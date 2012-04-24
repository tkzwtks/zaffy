# -*- coding: utf-8 -*-
from actionsetting import ActionSetting
from loadmodule import load_module_dir

class ActionLoader(object):
  def __init__(self):
    self.action_klasses = {}

  def create_action(self, raw_obj):
    if 'action' not in raw_obj:
      raise Exception("no action")
    action_name, method = raw_obj['action'].split(".")
    action_klass = self.get_action_klass(action_name)
    setting_obj = ActionSetting()
    del raw_obj['action']
    setting_obj.set_params(raw_obj, action_klass.default_params)
    setting_obj.set_method(method)
    action_obj = action_klass(setting_obj)
    return action_obj

  def load_actions(self):
    module_list = load_module_dir("actions")
    for module in module_list:
      module_name = module.__name__
      self.action_klasses[module_name] = getattr(module, module_name.title())

  def get_all_action_map(self):
    return self.action_klasses

  def get_action_klass(self, action_name):
    return self.action_klasses[action_name]

action_loader = ActionLoader()
