def all_check(str_to_check:str, inpt_list:list) -> str:
    for val in inpt_list:
        if not val.startswith(str_to_check):
            raise Exception(f"'{str_to_check}' not found in '{val}'")
    return str_to_check

def process(intp_:list) -> None:
    shortest = sorted(intp_,  key=len)[0]
    print(f"Using shortest string '{shortest}' to find common prefix.")
    out_ = '""'
    for i in range(len(shortest)):
        try:
            out_ = all_check(shortest[:i+1], intp_)
        except Exception as e:
            print(f"Mis-match: {e}")
            break
    print(f"The longest common prefix is: {out_}")

def get_input() -> list:
    raw_ = input("Enter input string separated by commas: ")
    cleaned_list = [x.strip() for x in  raw_.split(",")]
    return cleaned_list

if __name__ == "__main__":
    process(get_input())

