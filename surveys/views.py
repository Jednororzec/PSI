from django.shortcuts import render, HttpResponseRedirect
from .models import Survey
from django.contrib.auth.decorators import login_required
from . import forms
from django.urls import reverse
from django.contrib import messages


@login_required
def surveys(request):
    kwargs = {}
    kwargs['surveys'] = Survey.objects.filter(user=request.user)
    return render(request, 'surveys.html', kwargs)


@login_required
def create(request):
    if request.method == 'GET':
        kwargs = {}
        kwargs['survey_creation_form'] = forms.SurveyCreationForm(prefix='survey-creation-form')
        return render(request, 'create.html', kwargs)
    elif request.method == 'POST':
        form = forms.SurveyCreationForm(data=request.POST,
                                        prefix='survey-creation-form')
        if form.is_valid():
            new_survey = form.save(commit=False)
            new_survey.user = request.user
            new_survey.save()

            messages.success(request, "Wydarzenie zostało utworzone")
            return HttpResponseRedirect(reverse('survey',
                                                kwargs={
                                                    'survey_id': new_survey.id
                                                }))
        messages.error(request, "Nie prawidłowe wywołanie")
        return HttpResponseRedirect(reverse('surveys'))


@login_required
def survey(request, survey_id):
    try:
        user_survey = Survey.objects.get(id=survey_id)

        if request.method == 'GET':
            kwargs = {}
            kwargs['survey'] = user_survey
            kwargs['survey_edit_form'] = forms.SurveyCreationForm(prefix="survey-creation-form",
                                                                  instance=user_survey)
            return render(request, 'survey.html', kwargs)
        elif request.method == 'POST':
            form = forms.SurveyCreationForm(data=request.POST,
                                            prefix="survey-creation-form",
                                            instance=user_survey)
            if form.is_valid():
                form.save()
                messages.success(request, "Dane wydarzenia zostały zmienione")
                return HttpResponseRedirect(reverse('survey',
                                                    kwargs={
                                                        'survey_id': survey_id
                                                    }))
    except Survey.DoesNotExist:
        messages.error(request, "Takie wydarzenie nie istnieje.")
        return HttpResponseRedirect(reverse('surveys'))


@login_required
def delete(request, survey_id):
    try:
        user_survey = Survey.objects.get(id=survey_id)
        user_survey.delete()
        messages.success(request, "Wydarzenie zostało usunięte")
        return HttpResponseRedirect(reverse('surveys'))
    except Survey.DoesNotExist:
        messages.error(request, "Wydarzenie nie istnieje")
        return HttpResponseRedirect(reverse('surveys'))
