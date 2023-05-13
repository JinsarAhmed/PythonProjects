
import cv2

class AppError(BaseException):
  pass

def i2bin(i, l):
  actual = bin(i)[2:]
  if len(actual) > l:
    raise AppError("bit size is larger than expected.")

  while len(actual) < l:
    actual = "0"+actual

  return actual

def char2bin(c):
  return i2bin(ord(c), 8)

class LSB():

 
  MAX_BIT_LENGTH = 16

  def __init__(self, img):
    self.size_x, self.size_y, self.size_channel = img.shape

    self.image = img
    # pointer used to refer which cell on image will be read or write
    self.cur_x = 0
    self.cur_y = 0
    self.cur_channel = 0

 
  def next(self):
    if self.cur_channel != self.size_channel-1:
      self.cur_channel += 1
    else:
      self.cur_channel = 0
      if self.cur_y != self.size_y-1:
        self.cur_y += 1
      else:
        self.cur_y = 0
        if self.cur_x != self.size_x-1:
          self.cur_x += 1
        else:
          raise AppError("need larger image")


  def put_bit(self, bit):
    v = self.image[self.cur_x, self.cur_y][self.cur_channel]

    binaryV = bin(v)[2:]


    if binaryV[-1] != bit:
      binaryV = binaryV[:-1]+bit

    self.image[self.cur_x, self.cur_y][self.cur_channel] = int(binaryV,2)
    self.next()


  def put_bits(self, bits):
    for bit in bits:
      self.put_bit(bit)


  def read_bit(self):
    v = self.image[self.cur_x, self.cur_y][self.cur_channel]
    return bin(v)[-1]

  def read_bits(self, length):
    bits = ""
    for _ in range(0, length):
      bits += self.read_bit()
      self.next()

    return bits


  def embed(self, text):
    # calculate text length and convert it to binary with length 16 bit
    text_length = i2bin(len(text), self.MAX_BIT_LENGTH)
    # put length to first 16 cell
    self.put_bits(text_length)

    # put every character on text to image
    for c in text:
      # convert character into binary with 8 length
      bits = char2bin(c)
      # put every bit to cell respectively
      self.put_bits(bits)


  def extract(self):
   
    length = int(self.read_bits(self.MAX_BIT_LENGTH), 2)
    text = ""
    for _ in range(0, length):
      # read every 8 bit as a character
      c = int(self.read_bits(8), 2)
      # convert binary as a character
      text += chr(c)

    return text


  def save(self, dstPath):
    cv2.imwrite(dstPath, self.image)

if __name__ == "__main__":
  # obj = LSB(cv2.imread('src.jpg'))
  # obj.embed("I'm sure that one day everything will happen, you will love me and will never let me go I want to be with you, I want to love your flaws, always willing to make you happy no matter what happens, I promise I am...")

  obj = LSB(cv2.imread('dst.png'))
  text = obj.extract()
  print(text)
