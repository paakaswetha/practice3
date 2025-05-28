# university_data = {
#     "S101": {
#         "name": "Alice Johnson",
#         "major": "Computer Science",
#         "courses": {
#             "Python101": {"midterm": 88, "final": 92, "project": 94},
#             "Math201": {"midterm": 78, "final": 85, "project": 80}
#         }
#     },
#     "S102": {
#         "name": "Bob Smith",
#         "major": "Mathematics",
#         "courses": {
#             "Math201": {"midterm": 90, "final": 93, "project": 88},
#             "Stats101": {"midterm": 84, "final": 80, "project": 85}
#         }
#     },
#     "S103": {
#         "name": "Clara Lopez",
#         "major": "Physics",
#         "courses": {
#             "Physics101": {"midterm": 75, "final": 82, "project": 78},
#             "Math201": {"midterm": 70, "final": 72, "project": 68}
#         }
#     }
# }
# #to print student names and major
# for student_id,student_info in university_data.items():
#     name=student_info["name"]
#     major=student_info["major"]
#     print(f"Name:{name},Major:{major}")

# #average score per person per student
# for student_id,student_info in university_data.items():
#     courses=student_info["courses"]
#     average_score=0
#     num_courses=len(courses)
#     for grades,score in courses.items():
#         course_avg=sum(score.values())/len(score)
#         average_score+=course_avg
# overall_average=average_score/num_courses
# print(f"score of person:{}")
