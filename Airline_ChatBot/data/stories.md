## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## greet + compliment_employee + goodbye
* greet
  - utter_greet
* passengers_good_experience{"airline":"britishairway", "employee":"flight attendant", "positive":"thanks"}
  - utter_compliment_employee
* passengers_good_experience{"positive":"great"}
  - utter_compliment_thanks
* goodbye
  - utter_goodbye

## compliment_employee
* passengers_good_experience{"airline":"britishairway", "employee":"flight attendant", "positive":"thanks"}
  - utter_compliment_employee

## greet + compliment_airline + goodbye
* greet
  - utter_greet
* passengers_good_experience{"airline":"delta", "positive":"good"}
  - utter_compliment_airline
* passengers_good_experience{"positive":"great"}
  - utter_compliment_thanks
* goodbye
  - utter_goodbye

## compliment_airline
* passengers_good_experience{"airline":"delta", "positive":"good"}
  - utter_compliment_airline

## greet + happy_event_airline + goodbye
* greet
  - utter_greet
* passengers_good_experience{"airline": "southwestair", "event":"birthday", "positive":"good"}
  - utter_happy_event
* goodbye
  - utter_goodbye

## happy_event_airline
* passengers_good_experience{"airline": "southwestair", "event":"birthday", "positive":"good"}
  - utter_happy_event

## greet + happy_event + goodbye
* greet
  - utter_greet
* passengers_good_experience{"event":"birthday", "positive":"good"}
  - utter_happy_event
* goodbye
  - utter_goodbye

## greet + complain_employee + solution + goodbye
* greet
  - utter_greet
* passengers_bad_experience{"airline":"delta", "employee":"flight attendant", "negative":"worst"}
  - utter_complain_employee
* negative_experience
  - utter_solution_employee
* goodbye
  - utter_goodbye

## complain_employee + solution
* passengers_bad_experience{"airline":"delta", "employee":"flight attendant", "negative":"worst"}
  - utter_complain_employee
* negative_experience
  - utter_solution_employee

## greet + complain_airline + solution + goodbye
* greet
  - utter_greet
* passengers_bad_experience{"airline":"airasia", "negative":"worst"}
  - utter_complain_airline
* negative_experience
  - utter_solution_airline
* goodbye
  - utter_goodbye

## complain_airline + solution
* passengers_bad_experience{"airline":"airasia", "negative":"worst"}
  - utter_complain_airline
* negative_experience
  - utter_solution_airline