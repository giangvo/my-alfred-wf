
import alfred
if __name__ == "__main__":
    ACTION_MAPS = {1 : alfred.Action(1, gen_feed_back_method, do_plugin_action_method),
                    2 : alfred.Action(2, gen_feed_back_method, do_plugin_action_method)}
    alfred.Action.run(ACTION_MAPS)

    