from django.shortcuts import render
from django.template.loader import render_to_string, get_template
from django.http import HttpResponse
import random

import inspect
from datetime import datetime
from .forms import SimpleForm


def get_source(template_name):
    path = get_template(template_name).origin.name
    with open(path, "r") as source_file:
        return "".join(line for line in source_file)


# Create your views here.
def home(request):
    return render(
        request,
        "home.html",
        context={
            "view": inspect.getsource(now),
            "template": get_source("now.html"),
            "base": get_source("home_base.html"),
        },
    )


def now(request):
    now = datetime.now()
    return render(request, "now.html", context={"now": now})


def forms_page(request):
    form = SimpleForm()
    return render(
        request,
        "forms.html",
        context={
            "form": form,
            "view": inspect.getsource(forms),
            "template": get_source("forms_base.html"),
            "success": get_source("form_success.html"),
            "form_source": inspect.getsource(SimpleForm),
        },
    )


def forms(request):
    if request.method == "POST":
        form = SimpleForm(request.POST)
        if form.is_valid():
            summed = form.process()
            return render(request, "form_success.html", context={"summed": summed})
        return render(request, "forms_base.html", context={"form": form})
    else:
        form = SimpleForm()

    return render(request, "forms_base.html", context={"form": form})


def inline_page(request):
    form = SimpleForm()
    return render(
        request,
        "inline_page.html",
        context={
            "form": form,
            "view": inspect.getsource(inline_validate),
            "template": get_source("inline.html"),
            "first": get_source("inline_first.html"),
            "second": get_source("inline_second.html"),
        },
    )


def inline_validate(request, which):
    context = {"success": False, "error": False}
    if which == "first":
        value = request.POST.get("first-number")
        context["value"] = value
        if value:
            if int(value) % 2 == 0:
                context["success"] = True
            else:
                context["error"] = True
        return render(request, "inline_first.html", context=context)

    if which == "second":
        value = request.POST.get("second-number")
        context["value"] = value
        if value:
            if int(value) < 5:
                context["success"] = True
            else:
                context["error"] = True
        return render(request, "inline_second.html", context=context)


def modals_page(request):
    context = {
        "template": get_source("modals.html"),
        "modal": get_source("modal.html"),
        "view": inspect.getsource(modal),
    }
    return render(request, "modals_page.html", context=context)


def modal(request):
    return render(request, "modal.html")


def polling(request):
    context = {
        "progress": inspect.getsource(load),
        "initial": get_source("poller.html"),
        "load": get_source("load.html"),
    }
    return render(request, "polling.html", context=context)


def load(request):
    progress = int(request.GET.get("progress", 0))
    new_progress = progress + 10
    if new_progress == 100:
        return HttpResponse("Finished!", status=286)
    return render(request, "load.html", context={"progress": new_progress})


def out_of_bounds(request):
    context = {
        "template": get_source("out_of_bounds.html"),
        "response": get_source("task_performed.html"),
        "view": inspect.getsource(perform_task),
    }
    return render(request, "oob.html", context=context)


def perform_task(request):
    random_number = random.choice(range(50))
    return render(request, "task_performed.html", context={"id": random_number})


def miscellany(request):
    context = {"getsource": inspect.getsource(get_source)}
    return render(request, "miscellany.html", context=context)
