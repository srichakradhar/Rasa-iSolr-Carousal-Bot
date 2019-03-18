## mentioned series greet
* greet
  - utter_greet
* query{"series": "9500"}
    - slot{"series": "9500"}
    - action_response

## mentioned series wish
* wish
  - utter_wish
* query{"series": "9500"}
    - slot{"series": "9500"}
    - action_response

## mentioned series good bye
* wish
  - utter_wish
* query{"series": "9500"}
    - slot{"series": "9500"}
    - action_response
* thankyou
    - utter_goodbye

## not mentioned series greet
* greet
  - utter_greet
* query
  - utter_ask_series
* query{"series": "9300"}
    - slot{"series": "9300"}
    - action_response

## not mentioned series greet good bye
* greet
  - utter_greet
* query
  - utter_ask_series
* query{"series": "9300"}
    - slot{"series": "9300"}
    - action_response
* thankyou
    - utter_goodbye

## not mentioned series wish
* wish
  - utter_wish
* query
  - action_response
* query{"series": "9500"}
    - slot{"series": "9500"}
    - action_response

## not mentioned series wish
* wish
  - utter_wish
* query
  - action_response
* query{"series": "9500"}
    - slot{"series": "9500"}
    - action_response
* thankyou
    - utter_goodbye

## happy path
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* mood_affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* mood_deny
  - utter_goodbye

## goodbye
* goodbye
 - utter_goodbye