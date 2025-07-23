# am/place

am/place is an interactive game inspired by [r/place](https://en.wikipedia.org/wiki/R/place) built by amFOSS members for Hacktoberfest 2024. The way it works is that players submit PR's to this repository modifying the `pixel_update.json` file, the modifications to this file will reflect on pixels on the cavas.

`pixel_update.json`:
```json
[
  {
    "x": "69",
    "y": "42",
    "rgb": "#8008ff"
  },
  {
    "x": "70",
    "y": "7",
    "rgb": "#222222"
  },
  {
    "x": "71",
    "y": "8",
    "rgb": "#333333"
  },
  {
    "x": "72",
    "y": "9",
    "rgb": "#444444"
  },
  {
    "x": "68",
    "y": "5",
    "rgb": "#555555"
  }
]
```

Each entry in this json list corresponds to a singular pixel on the canvas. There are a few rules to be followed when making PR's:
1. Only `pixel_update.json` should have modifications, you can verify this by running `git diff` before commiting.
2. The above prescribed format must be strictly followed.
3. You're only allowed to modify 5 pixels at a time.

Failure to follow any of the above rules will result in your PR getting disqualified, we have setup a Github action which accepts and rejects PR's automagically. You can try out this game at [PLACEHOLDER]

## 2024 Canvas:
![image](https://github.com/user-attachments/assets/e3cb0ab1-8a1f-41dc-b629-3b173ea829fc)


## Credits:
Backend Author: [@Rihaan B H](https://github.com/RihaanBH-1810)

Frontend Author: [@JATAYU000](https://github.com/JATAYU000)

Misc Fixes: [@Hridesh MG](https://github.com/hrideshmg)
