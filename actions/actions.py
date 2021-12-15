from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionTellNameRole(Action):

    def name(self) -> Text:
        return "action_tell_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = str(tracker.get_slot('role')).lower()
        print(name)

        if name == 'chủ tịch':
            dispatcher.utter_message(text="Chủ tịch của công ty là Bác Kim ạ!")
        elif name == 'giám đốc':
            dispatcher.utter_message(text="Giám đốc của công ty là anh Hiền ạ!")
        elif name == 'techlead':
            dispatcher.utter_message(text="Techlead của công ty mình là anh Duy ạ!")
        elif name == 'ai':
            dispatcher.utter_message(text="Leader của team AI là anh Tiến Dũng ạ!")
        elif name == 'web':
            dispatcher.utter_message(text="Leader của team WEB là anh .., ạ!")
        else: 
            dispatcher.utter_message(text="Xin lỗi vấn đề này đã vượt tầm hiểu biết của em ạ :((")

        return []

class ActionTellPassWifi(Action):
    
    def name(self) -> Text:
        return "action_tell_pass_wifi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        wifi = str(tracker.get_slot('wifi')).lower()
        print(wifi)

        if wifi == 'mirai':
            dispatcher.utter_message(text="Password của wifi Mirai là 12345678 ạ!")
        elif wifi == 'grooodev5':
            dispatcher.utter_message(text="Password của wifi Mirai là 12345678 ạ!")
        else: 
            dispatcher.utter_message(text="Xin lỗi vấn đề này đã vượt tầm hiểu biết của em ạ :((")

        return []
