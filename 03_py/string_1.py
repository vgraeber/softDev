def hello_name(name):
  return 'Hello ' + name + '!'

def make_abba(a, b):
  return a + b + b + a

def make_tags(tag, word):
  return "<" + tag + ">" + word + "</" + tag + ">"

def make_out_word(out, word):
  s1 = out[:2]
  s2 = out[2:]
  return s1 + word + s2

def extra_end(str):
  e = str[-2:]
  return e * 3

def first_two(str):
  return str[:2]

def first_half(str):
  return str[:(len(str)/2)]

def without_end(str):
  return str[1:-1]

def combo_string(a, b):
  if (len(a) > len(b)):
    return b + a + b
  else :
    return a + b + a

def non_start(a, b):
  return a[1:] + b[1:]

def left2(str):
  spl1 = str[:2]
  spl2 = str[2:]
  return (spl2 + spl1)