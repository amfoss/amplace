from flask import Flask, jsonify, request
from Models import Session, Pixel, User
from config import config
from datetime import datetime, timedelta
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


app.secret_key = config["APP_SECRET_KEY"]

def check_cooldown(pixel):
    session = Session()
    try:
        flag = True
        existing_pixel = session.query(Pixel).filter_by(x=pixel["X"], y=pixel["Y"]).order_by(Pixel.updated_at.desc()).first()

        if existing_pixel:
            last_updated_time = existing_pixel.updated_at
            if last_updated_time > datetime.utcnow() - timedelta(minutes=2):
                flag = False
        
    finally:
        session.close()
        return flag

@app.route("/api/update_pixel", methods=['POST'])
@cross_origin()
def update_pixel():
    if request.method == "POST":
        try:
            cooldown_pixels = []
            data = request.json
            session = Session()
            pixel_list = data["pixel_list"]
            username = data["user"]

            for pixel_data in pixel_list:
                
                user = session.query(User).filter_by(username=username).first()
                if not user:
                    user = User(username=username)
                    session.add(user)
                    session.commit()  
                
                existing_pixel = session.query(Pixel).filter_by(x=pixel_data["X"], y=pixel_data["Y"]).first()

                if existing_pixel:
                    if check_cooldown(pixel_data):
                        existing_pixel.color_hex = pixel_data["hex-code"]
                        existing_pixel.updated_at = datetime.utcnow()
                        existing_pixel.user = user
                        user.count += 1
                        session.add(user)
                    else:
                        cooldown_pixels.append(pixel_data)

                else:
                    new_pixel = Pixel(
                        user_id=user.username,
                        x=pixel_data["X"],
                        y=pixel_data["Y"],
                        color_hex=pixel_data["hex-code"],
                        updated_at=datetime.utcnow()
                    )
                    user.count += 1

                    session.add(user)
                    session.add(new_pixel)
            session.commit()
            if len(cooldown_pixels) == 0:
                return jsonify({"success": True, "message" : "All pixels updated none blocked by a cooldown"}), 200
            elif len(cooldown_pixels) == len(pixel_list):
                return jsonify({"success" : True, "message": "All the pixels you tried to update have a cooldown try again in 2 min"}), 200
            else:
                return jsonify({"success" : True, "message" : f" the following pixels that you tried to update have a cooldown {cooldown_pixels}"}), 200

        except Exception as e:
            session.rollback() 
            return jsonify({"success": False, "message": str(e)}), 404
        finally:
            session.close()

@app.route("/api/get_pixel", methods=["GET"])
def get_pixel_details():
    if request.method == "GET":
        try:
            session = Session()
            pixels = session.query(Pixel).all()

            pixel_list = [
                {
                    "user": pixel.user_id,
                    "X": pixel.x,
                    "Y": pixel.y,
                    "hex-code": pixel.color_hex,
                    "updated_at": pixel.updated_at.strftime("%Y-%m-%d %H:%M:%S")
                }
                for pixel in pixels
            ]

            return jsonify({"success": True, "pixels": pixel_list}), 200

        except Exception as e:
            return jsonify({"success": False, "message": str(e)}), 404

        finally:
            session.close()

@app.route("/api/get_user_details", methods=["GET"])
def get_user_details():
    if request.method == "GET":
        try:
            session = Session()
            users =  session.query(User).all()

            users_data_list = [
                {
                    "user" : user.username,
                    "score" : user.count
                }
                for user in users
            ]
            return jsonify({"success": True, "user_data": users_data_list}), 200

        except Exception as e:
            return jsonify({"success": False, "message": str(e)}), 404

        finally:
            session.close()

@app.route("/api/delete_pixel", methods=['DELETE'])
def delete_pixel():
    if request.method == "DELETE":
        try:
            data = request.json
            session = Session()
            x = data.get("X")
            y = data.get("Y")
            if x is None or y is None:
                return jsonify({"success": False, "message": "X and Y coordinates are required"}), 400

            pixel = session.query(Pixel).filter_by(x=x, y=y).first()

            if not pixel:
                return jsonify({"success": False, "message": "Pixel not found"}), 404

            session.delete(pixel)
            session.commit()

            return jsonify({"success": True, "message": "Pixel deleted successfully"}), 200

        except Exception as e:
            session.rollback()
            return jsonify({"success": False, "message": str(e)}), 500

        finally:
            session.close()


if __name__ == "__main__":
    app.run(debug=True)
