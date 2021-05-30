# tarpolando REST API

#### Prerequisites

Python 3

#### Start the server

```
python main.py
```

#### Resource 1

Request

```
http://127.0.0.1:5000/items-by-category/from-date-range?start=2021-01-28&end=2022-01-28
```

Response

```json
{
  "items": [
    {
      "address": "18 Wall St Central Business District",
      "allDay": 0,
      "author": "Jack Stokes",
      "authorAvatarUrl": "",
      "commentsEnabled": false,
      "content": " <div class=\"texte\" > <p>Open Mic Standup Comedy Night</p> <p>Every Monday</p> <p>Sign up 8:30pm</p> <p>Showtime 9pm</p> <p>The Other Bar - at Wall Street Plaza</p> <p>&nbsp;</p> <p><a href=\"\">RSVP</a></p> <p><a href=\"https://eventbrite.com\">Buy Tickets</a></p> </div> <div class=\"photo top\" style=\"text-align:center\"> <a href=\"https://cmsphoto.ww-cdn.com/superstatic/1966303/art/grande/41626562-34937919.jpg?v=1578688667\" target=\"_blank\"> <img id=\"img-41626562-34937919\" src=\"https://cmsphoto.ww-cdn.com/superstatic/1966303/art/default/41626562-34937919.jpg?v=1578688667\" alt=\"OPEN MIC STANDUP COMEDY NIGHT\" title=\"OPEN MIC STANDUP COMEDY NIGHT\" /> </a> </div> ",
      "date": "2021-01-28T02:30:00+01:00",
      "email": "",
      "endDate": "2022-01-28T02:30:00+01:00",
      "id": 41626562,
      "images": [
        {
          "id": "img-41626562-34937919",
          "otherImagesUrl": {
            "large": "https://cmsphoto.ww-cdn.com/superstatic/1966303/art/grande/41626562-34937919.jpg?v=1578688667"
          },
          "url": "https://cmsphoto.ww-cdn.com/superstatic/1966303/art/default/41626562-34937919.jpg?v=1578688667"
        }
      ],
      "isFeatured": "img-41626562-34937919",
      "isHeadline": 0,
      "largeThumbnail": "https://cmsphoto.ww-cdn.com/superstatic/1966303/art/large_x2_16_9/41626562-34937919.jpg?v=1578688667",
      "latitude": "28.542542",
      "longitude": "-81.3786204",
      "meta": {
        "description": "",
        "title": ""
      },
      "originalThumbnail": "https://cmsphoto.ww-cdn.com/superstatic/1966303/art/grande/41626562-34937919.jpg?v=1578688667",
      "phoneNumber": "",
      "smallThumbnail": "https://cmsphoto.ww-cdn.com/superstatic/1966303/art/imagette_16_9/41626562-34937919.jpg?v=1578688667",
      "sortDate": "2021-05-19T02:30:00+02:00",
      "subsections": {
        "33292120": [
          "Main category"
        ],
        "33292145": [
          "Main category"
        ]
      },
      "subtype": "mcms",
      "summary": "Open Mic Standup Comedy Night",
      "thumbnail": "https://cmsphoto.ww-cdn.com/superstatic/1966303/art/large_16_9/41626562-34937919.jpg?v=1578688667",
      "title": "OPEN MIC STANDUP COMEDY NIGHT",
      "type": "event",
      "url": "https://web.thetaporlando.com/top-picks/i/41626562/open-mic-standup-comedy-night",
      "urlEvent": "",
      "urlShop": "",
      "xLargeThumbnail": "https://cmsphoto.ww-cdn.com/resizeapi/4a40be80d7fca74b4d4f0ac70f106b204753b492/1200/-1/",
      "xxLargeThumbnail": "https://cmsphoto.ww-cdn.com/resizeapi/4a40be80d7fca74b4d4f0ac70f106b204753b492/3200/-1/"
    }
  ]
}
```

#### Resource 2

Request 1: Existing event ID

```
http://127.0.0.1:5000/items-by-category/from-id?id=39689198
```

Response

```json
{
  "address": "33 E Pine St Central Business District",
  "allDay": 0,
  "author": "Jack Stokes",
  "authorAvatarUrl": "",
  "commentsEnabled": false,
  "content": " <div class=\"texte\" > <p>MAD HOUSE FRIDAYS</p> <p>Every Friday</p> <p>No Cover</p> <p>$200 Tito Magnum Bottles</p> <p>$3 Jameson &amp; Green Tea</p> <p>$6 Crown Apple, Johnny Red &amp; Smirnoff Flavors</p> <p>Bullitt Bar Orlando</p> </div> <div class=\"photo top\" style=\"text-align:center\"> <a href=\"https://cmsphoto.ww-cdn.com/superstatic/1966303/art/grande/39689198-34047385.jpg?v=1574118970\" target=\"_blank\"> <img id=\"img-39689198-34047385\" src=\"https://cmsphoto.ww-cdn.com/superstatic/1966303/art/default/39689198-34047385.jpg?v=1574118970\" alt=\"MAD HOUSE FRIDAYS\" title=\"MAD HOUSE FRIDAYS\" /> </a> </div> ",
  "date": "2021-02-01T03:00:00+01:00",
  "email": "",
  "endDate": "2022-01-31T08:00:00+01:00",
  "id": 39689198,
  "images": [
    {
      "id": "img-39689198-34047385",
      "otherImagesUrl": {
        "large": "https://cmsphoto.ww-cdn.com/superstatic/1966303/art/grande/39689198-34047385.jpg?v=1574118970"
      },
      "url": "https://cmsphoto.ww-cdn.com/superstatic/1966303/art/default/39689198-34047385.jpg?v=1574118970"
    }
  ],
  "isFeatured": "img-39689198-34047385",
  "isHeadline": 0,
  "largeThumbnail": "https://cmsphoto.ww-cdn.com/superstatic/1966303/art/large_x2_16_9/39689198-34047385.jpg?v=1574118970",
  "latitude": "28.5413885",
  "longitude": "-81.3782758",
  "meta": {
    "description": "",
    "title": ""
  },
  "originalThumbnail": "https://cmsphoto.ww-cdn.com/superstatic/1966303/art/grande/39689198-34047385.jpg?v=1574118970",
  "phoneNumber": "",
  "smallThumbnail": "https://cmsphoto.ww-cdn.com/superstatic/1966303/art/imagette_16_9/39689198-34047385.jpg?v=1574118970",
  "sortDate": "2021-05-14T03:00:00+02:00",
  "subsections": {
    "33292120": [
      "Main category"
    ],
    "33292145": [
      "Main category"
    ],
    "33292148": [
      "Main category"
    ]
  },
  "subtype": "mcms",
  "summary": "MAD HOUSE FRIDAYS",
  "thumbnail": "https://cmsphoto.ww-cdn.com/superstatic/1966303/art/large_16_9/39689198-34047385.jpg?v=1574118970",
  "title": "MAD HOUSE FRIDAYS",
  "type": "event",
  "url": "https://web.thetaporlando.com/top-picks/i/39689198/mad-house-fridays",
  "urlEvent": "",
  "urlShop": "",
  "xLargeThumbnail": "https://cmsphoto.ww-cdn.com/resizeapi/39df734eafb3a803c201e4db2fe6524171c0e881/1200/-1/",
  "xxLargeThumbnail": "https://cmsphoto.ww-cdn.com/resizeapi/39df734eafb3a803c201e4db2fe6524171c0e881/3200/-1/"
}
```

Request 2: Non-existing event ID

```
http://127.0.0.1:5000/items-by-category/from-id?id=3968919
```

Response

```json
{}
```