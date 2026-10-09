def submit(request, course_id):
        course = get_object_or_404(Course, pk=course_id)
        user = request.user
        enrollment = Enrollment.objects.get(user=user, course=course)
        submission = Submission.objects.create(enrollment=enrollment)
        choices = extract_answers(request)
        submission.choices.set(choices)
        submission_id = submission.id
        return HttpResponseRedirect(reverse(viewname='onlinecourse:exam_result', args=(course_id, submission_id,)))



# An example method to collect the selected choices from the exam form from the request object
def extract_answers(request):
   submitted_anwsers = []
   for key in request.POST:
       if key.startswith('choice'):
           value = request.POST[key]
           choice_id = int(value)
           submitted_anwsers.append(choice_id)
   return submitted_anwsers
def show_exam_result(request, course_id, submission_id):
		context = {}
		course = get_object_or_404(Course, pk=course_id)
		submission = Submission.objects.get(id=submission_id)
		choices = submission.choices.all()

		total_score = 0
		questions = course.question_set.all()  # Assuming course has related questions

		for question in questions:
			correct_choices = question.choice_set.filter(is_correct=True)  # Get all correct choices for the question
			selected_choices = choices.filter(question=question)  # Get the user's selected choices for the question

			# Check if the selected choices are the same as the correct choices
			if set(correct_choices) == set(selected_choices):
				total_score += question.grade  # Add the question's grade only if all correct answers are selected

		context['course'] = course
		context['grade'] = total_score
		context['choices'] = choices

		return render(request, 'onlinecourse/exam_result_bootstrap.html', context)

