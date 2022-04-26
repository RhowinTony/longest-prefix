# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

class LongestPrefix:
   def __init__(self, inpt_string:str) -> None:
      self.input_string_list = inpt_string.split(",")
      
   def process(self) -> str:
      substring_list = self._create_substring()
      output_val = ""
      for element in substring_list:
         for inpt_string in self.input_string_list:
            if inpt_string.startswith(element):
               output_val = element
            else:
               break
      return output_val


   def _create_substring(self) -> list:
      sorted_list = sorted(self.input_string_list)
      output_list = []
      for i, char_ in enumerate(sorted_list[0]):
         output_list.append(sorted_list[0][:i+1])

      return output_list

def get_user_data(input_data):
   # str_data = []
   # e = 0
   # while e < input_data:
   #    val = input("- Enter a word - ")
   #    e += 1
   #    str_data.append(val)
   raw_string = ""


def process():
   # 1.loop to get incremental substrings from 1st input string - ex: fall - f, fa ,fal, fall
   # 2.input is outpt of 1  
   pass



input_ = input("Enter strings separated by comma: ")
prefix_finder = LongestPrefix(input_)
output = prefix_finder.process()
print(f"Longest prefix is {output}")
