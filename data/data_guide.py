# -*- coding: utf-8 -*-
"""data_guide.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/174vlM_VQyL7WnFvNxklCFx_99-Jy9v0Z

For this model we used TM-1-2019 data of Taskmaster dataset that is available on github for training
"""

# Steps to get the data
# Clone the Taskmaster repository
!git clone https://github.com/google-research-datasets/Taskmaster.git

#some sample dialogue are as follows
{
    "conversation_id": "dlg-00055f4e-4a46-48bf-8d99-4e477663eb23",
    "instruction_id": "restaurant-table-2",
    "utterances": [
      {
        "index": 0,
        "speaker": "USER",
        "text": "Hi, I'm looking to book a table for Korean food."
      },
      {
        "index": 1,
        "speaker": "ASSISTANT",
        "text": "Ok, what area are you thinking about?"
      },
      {
        "index": 2,
        "speaker": "USER",
        "text": "Somewhere in Southern NYC, maybe the East Village?",
        "segments": [
          {
            "start_index": 13,
            "end_index": 49,
            "text": "Southern NYC, maybe the East Village",
            "annotations": [
              {
                "name": "restaurant_reservation.location.restaurant.accept"
              }
            ]
          },
          {
            "start_index": 13,
            "end_index": 25,
            "text": "Southern NYC",
            "annotations": [
              {
                "name": "restaurant_reservation.location.restaurant.accept"
              }
            ]
          }
        ]
      },
      {
        "index": 3,
        "speaker": "ASSISTANT",
        "text": "Ok, great.  There's Thursday Kitchen, it has great reviews.",
        "segments": [
          {
            "start_index": 20,
            "end_index": 35,
            "text": "Thursday Kitche",
            "annotations": [
              {
                "name": "restaurant_reservation.name.restaurant.reject"
              }
            ]
          }
        ]
      },
      {
        "index": 4,
        "speaker": "USER",
        "text": "That's great. So I need a table for tonight at 7 pm for 8 people. We don't want to sit at the bar, but anywhere else is fine.",
        "segments": [
          {
            "start_index": 26,
            "end_index": 31,
            "text": "table",
            "annotations": [
              {
                "name": "restaurant_reservation.type.seating"
              }
            ]
          },
          {
            "start_index": 47,
            "end_index": 51,
            "text": "7 pm",
            "annotations": [
              {
                "name": "restaurant_reservation.time.reservation"
              },
              {
                "name": "restaurant_reservation.time.reservation"
              }
            ]
          },
          {
            "start_index": 56,
            "end_index": 57,
            "text": "8",
            "annotations": [
              {
                "name": "restaurant_reservation.num.guests"
              },
              {
                "name": "restaurant_reservation.num.guests"
              }
            ]
          },
          {
            "start_index": 87,
            "end_index": 98,
            "text": "at the bar,",
            "annotations": [
              {
                "name": "restaurant_reservation.type.seating"
              }
            ]
          }
        ]
      },
      {
        "index": 5,
        "speaker": "ASSISTANT",
        "text": "They don't have any availability for 7 pm.",
        "segments": [
          {
            "start_index": 37,
            "end_index": 41,
            "text": "7 pm",
            "annotations": [
              {
                "name": "restaurant_reservation.time.reservation"
              }
            ]
          },
          {
            "start_index": 37,
            "end_index": 42,
            "text": "7 pm.",
            "annotations": [
              {
                "name": "restaurant_reservation.time.reservation.reject"
              }
            ]
          }
        ]
      },
      {
        "index": 6,
        "speaker": "USER",
        "text": "What times are available?"
      },
      {
        "index": 7,
        "speaker": "ASSISTANT",
        "text": "5 or 8.",
        "segments": [
          {
            "start_index": 0,
            "end_index": 1,
            "text": "5",
            "annotations": [
              {
                "name": "restaurant_reservation.time.reservation"
              },
              {
                "name": "restaurant_reservation.time.reservation"
              }
            ]
          },
          {
            "start_index": 5,
            "end_index": 6,
            "text": "8",
            "annotations": [
              {
                "name": "restaurant_reservation.time.reservation"
              },
              {
                "name": "restaurant_reservation.time.reservation"
              }
            ]
          }
        ]
      },
      {
        "index": 8,
        "speaker": "USER",
        "text": "Yikes, we can't do those times."
      },
      {
        "index": 9,
        "speaker": "ASSISTANT",
        "text": "Ok, do you have a second choice?"
      },
      {
        "index": 10,
        "speaker": "USER",
        "text": "Let me check."
      },
      {
        "index": 11,
        "speaker": "ASSISTANT",
        "text": "Ok."
      },
      {
        "index": 12,
        "speaker": "USER",
        "text": "Lets try Boka, are they free for 8 people at 7?",
        "segments": [
          {
            "start_index": 9,
            "end_index": 13,
            "text": "Boka",
            "annotations": [
              {
                "name": "restaurant_reservation.name.restaurant.accept"
              },
              {
                "name": "restaurant_reservation.name.restaurant.accept"
              }
            ]
          },
          {
            "start_index": 33,
            "end_index": 34,
            "text": "8",
            "annotations": [
              {
                "name": "restaurant_reservation.num.guests.accept"
              },
              {
                "name": "restaurant_reservation.num.guests.accept"
              }
            ]
          },
          {
            "start_index": 45,
            "end_index": 46,
            "text": "7",
            "annotations": [
              {
                "name": "restaurant_reservation.time.reservation.accept"
              },
              {
                "name": "restaurant_reservation.time.reservation.accept"
              }
            ]
          }
        ]
      },
      {
        "index": 13,
        "speaker": "ASSISTANT",
        "text": "Yes."
      },
      {
        "index": 14,
        "speaker": "USER",
        "text": "Great, let's book that."
      },
      {
        "index": 15,
        "speaker": "ASSISTANT",
        "text": "Ok great, are there any other requests?"
      },
      {
        "index": 16,
        "speaker": "USER",
        "text": "No, that's it, just book."
      },
      {
        "index": 17,
        "speaker": "ASSISTANT",
        "text": "Great, should I use your account you have open with them?"
      },
      {
        "index": 18,
        "speaker": "USER",
        "text": "Yes please."
      },
      {
        "index": 19,
        "speaker": "ASSISTANT",
        "text": "Great. You will get a confirmation to your phone soon."
      }
    ]
  }