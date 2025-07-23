## delete pixel
DELETE http://localhost:5000/api/delete_pixel
Content-Type: application/json

{ "X":9,
  "Y":15
}

## Test get user details
GET http://localhost:5000/api/get_user_details

## Test updating pixels 
POST http://localhost:5000/api/update_pixel
Content-Type: application/json

{ "user" : "test_user",
  "pixel_list": [
    {
      "X": 10,
      "Y": 15,
      "hex-code": "#ff5733"
    },
    {
      "X": 12,
      "Y": 18,
      "hex-code": "#33c5ff"
    },
    {
      "X": 10,
      "Y": 15,
      "hex-code": "#123456"
    },
    {
      "X": 9,
      "Y": 15,
      "hex-code": "#123456"
    }
  ]
}

##  Test getting pixel details 
GET http://localhost:5000/api/get_pixel

---
Author: [@Rihaan B H](https://github.com/RihaanBH-1810)
