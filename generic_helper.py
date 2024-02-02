import re


def extract_session_id(session_str: str):

    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_str = match.group(1)
        return extracted_str

    return ""

def get_str_from_food_dict(food_dict: dict):
    return ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])

if __name__ == "__main__":
    print(get_str_from_food_dict({"samosa": 2, "chole": 5}))
    # print(extract_session_id("projects/flavorchat-twkc/agent/sessions/2fef7ce5-9c91-8501-ebcc-26411da04f71/contexts/ongoing-order"))
