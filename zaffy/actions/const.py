# -*- coding: utf-8 -*-
from baseaction import BaseAction


class _MetaConst(type):
  def __getattribute__(cls, name):
    return type.__getattribute__(cls, 'const_params')[name]


class Const(BaseAction):
  __metaclass__ = _MetaConst

  const_params = {}

  @classmethod
  def setup(cls, config):
    type.__setattr__(cls, 'const_params', config)

  def do_const(self, **kwargs):
    self.do_set(**kwargs)

  def do_set(self, **kwargs):
    for key, value in kwargs.items():
      if key in self.const_params:
        raise Exception("cannot overridden const key '{0}', value '{1}'".format(key, value))
      self.const_params[key] = value

    self.result = self.const_params

