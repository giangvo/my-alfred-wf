import json
import sys
from subprocess import Popen, PIPE
class Action(object):
    part = 0
    do_generate_feedbacks = None
    do_execute = None
    def __init__(self, part, do_generate_feedbacks, do_execute):
        self.part = part
        self.do_generate_feedbacks = do_generate_feedbacks
        self.do_execute = do_execute

    def execute(self, query):
        self.do_execute(query)

    def generate_feedbacks(self, query):
        feedback = self.do_generate_feedbacks(query, self.part)
        feedback.output()

    @staticmethod
    def run(action_map):
        action = sys.argv[1].strip() if len(sys.argv) > 1 else ""
        query = sys.argv[2].strip() if len(sys.argv) > 2 else ""    
        if action == "generate_feedbacks":
            count = len(query.split(">"))
            action_map[count].generate_feedbacks(query)
        elif action == "execute":
            query_obj = Action.from_json_str(query)
            part = query_obj["part"]
            action_map[int(part)].execute(query)

    @staticmethod
    def run_applescript(script):
        if hasattr(script, "encode"):
            script = script.encode("utf-8")

        osa = Popen(["osascript", "-"], stdout=PIPE, stdin=PIPE, stderr=PIPE)
        results, err = osa.communicate(script)
        
        if err:
            raise Exception(err)
        
        return results.decode("utf-8")

    @staticmethod
    def to_json_str(data):
        return json.dumps(data)
    @staticmethod
    def from_json_str(json_str):
        return json.loads(json_str)
    @staticmethod
    def get_field(json_str, field):
        return json.loads(json_str)[field]



