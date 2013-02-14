# -*- coding: utf-8 -*-
import requests
from baseaction import BaseAction


class Http(BaseAction):
  """ Http アクション

  http リクエストに関する処理を行なう
  """
  def _create_result(self, response, no_content, binary_content, save_file):
    result = {}
    result['status'] = response.status_code
    result['headers'] = response.headers
    result['encoding'] = response.encoding
    result['cookies'] = response.cookies
    result['content'] = self._create_content(response, no_content, binary_content, save_file)
    return result

  def _create_content(self, response, no_content, binary_content, save_file):
    if not no_content:
      if save_file:
        # ファイルに保存する場合は自動的にバイナリ保存
        fp = open(save_file, "wb")
        for line in response.iter_content():
          fp.write(line)
        fp.close()
      else:
        return response.content if binary_content else response.text
    return ''

  def _http_method(self, method, url, headers, cookies, params, data,
      no_content, binary_content, save_file, ssl_verify, allow_redirects, timeout):

    r = getattr(requests, method)(url,
          headers=headers,
          cookies=cookies,
          params=params,
          data=data,
          verify=ssl_verify,
          allow_redirects=allow_redirects,
          timeout=timeout)
    self.result = self._create_result(r, no_content, binary_content, save_file)

  def do_delete(self, url, headers={}, cookies={}, params={}, data={}, no_content=False,
      binary_content=False, save_file=None, ssl_verify=True, allow_redirects=True, timeout=None):
    """
    :param bool no_content: True にすると header のみ取得する
    :param bool binary_content: content をバイナリとして取得する
    :param string save_file: content をファイルに保存してメモリ上に持たない (binary_content=Trueとして扱う)
    :param bool ssl_verify: SSL 証明書のチェックをするか（自己証明書の場合はFalseじゃないと通らない）
    :param bool allow_redirects: 自動でリダイレクトするか
    :param int timeout: タイムアウト時間を秒数で指定する（content のダウンロードに要する時間は除く）
    :return: - **status** (*int*) - http response status
             - **content** (*string*) - http body
    """
    method_params = locals()
    del method_params['self']
    self._http_method("delete", **method_params)

  def do_get(self, url, headers={}, cookies={}, params={}, data={}, no_content=False,
      binary_content=False, save_file=None, ssl_verify=True, allow_redirects=True, timeout=None):
    """ get """
    method_params = locals()
    del method_params['self']
    self._http_method("get", **method_params)

  def do_post(self, url, headers={}, cookies={}, params={}, data={}, no_content=False,
      binary_content=False, save_file=None, ssl_verify=True, allow_redirects=True, timeout=None):
    """ post """
    method_params = locals()
    del method_params['self']
    self._http_method("post", **method_params)

  def do_put(self, url, headers={}, cookies={}, params={}, data={}, no_content=False,
      binary_content=False, save_file=None, ssl_verify=True, allow_redirects=True, timeout=None):
    """ put """
    method_params = locals()
    del method_params['self']
    self._http_method("put", **method_params)

  def do_head(self, url, headers={}, cookies={}, params={}, data={}, no_content=False,
      binary_content=False, save_file=None, ssl_verify=True, allow_redirects=True, timeout=None):
    """ head """
    method_params = locals()
    del method_params['self']
    self._http_method("head", **method_params)

  def do_patch(self, url, headers={}, cookies={}, params={}, data={}, no_content=False,
      binary_content=False, save_file=None, ssl_verify=True, allow_redirects=True, timeout=None):
    """ patch """
    method_params = locals()
    del method_params['self']
    self._http_method("patch", **method_params)

