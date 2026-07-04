from prompts.easy_prompt import get_easy_prompt
from prompts.exam_prompt import get_exam_prompt
from prompts.interview_prompt import get_interview_prompt
from prompts.student_prompt import get_student_prompt


def get_prompt(mode):

    if mode == "Easy Mode":
        return get_easy_prompt()

    elif mode == "Exam Mode":
        return get_exam_prompt()

    elif mode == "Interview Mode":
        return get_interview_prompt()

    elif mode == "Student Mode":
        return get_student_prompt()

    else:
        raise ValueError("Invalid Mode")
