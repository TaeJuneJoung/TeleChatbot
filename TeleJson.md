# TeleChatbot
Telegram Chat Bot​:robot:​

## API의 JSON형태

## text, file, photo일 때 접근방식

#### text
```json
{
   "update_id": ,
   "message": {
      "message_id": ,
      "from": {
         "id": ,
         "is_bot": false,
         "first_name": "TaeJune",
         "last_name": "Joung",
         "language_code": "ko"
      },
      "chat": {
         "id": ,
         "first_name": "TaeJune",
         "last_name": "Joung",
         "type": "private"
      },
      "date": ,
      "text": "테스트"
   }
}
```

#### photo
```json
{
   "update_id": ,
   "message": {
      "message_id": ,
      "from": {
         "id": ,
         "is_bot": false,
         "first_name": "TaeJune",
         "last_name": "Joung",
         "language_code": "ko"
      },
      "chat": {
         "id": ,
         "first_name": "TaeJune",
         "last_name": "Joung",
         "type": "private"
      },
      "date": ,
      "photo": [
         {
            "file_id": "",
            "file_size": ,
            "width": ,
            "height": 
         },
         {
            "file_id": "",
            "file_size": ,
            "width": ,
            "height": 
         },
         {
            "file_id": "",
            "file_size": ,
            "width": ,
            "height": 
         },
         {
            "file_id": "",
            "file_size": ,
            "width": ,
            "height": 
         }
      ],
      "caption": ""
   }
}
```

#### video
```json
{
   "update_id": ,
   "message": {
      "message_id": ,
      "from": {
         "id": ,
         "is_bot": false,
         "first_name": "TaeJune",
         "last_name": "Joung",
         "language_code": "ko"
      },
      "chat": {
         "id": ,
         "first_name": "TaeJune",
         "last_name": "Joung",
         "type": "private"
      },
      "date": ,
      "video": {
         "duration": ,
         "width": ,
         "height": ,
         "mime_type": "video/mp4",
         "thumb": {
            "file_id": "",
            "file_size": ,
            "width": ,
            "height": 
         },
         "file_id": "",
         "file_size": 
      }
   }
}
```

#### file
```json
{
   "update_id": ,
   "message": {
      "message_id": ,
      "from": {
         "id": ,
         "is_bot": false,
         "first_name": "TaeJune",
         "last_name": "Joung",
         "language_code": "ko"
      },
      "chat": {
         "id": ,
         "first_name": "TaeJune",
         "last_name": "Joung",
         "type": "private"
      },
      "date": ,
      "document": {
         "file_name": ".JPG",
         "mime_type": "image/jpeg",
         "thumb": {
            "file_id": "",
            "file_size": ,
            "width": ,
            "height": 
         },
         "file_id": "",
         "file_size": 
      }
   }
}
```

이 외에 location/대화상대(연락처)/이모티콘/녹음파일 등... 있다
다중파일은 단일파일을 여러번 보내는 형식


