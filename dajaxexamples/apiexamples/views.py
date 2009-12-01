from django.shortcuts import render_to_response

def api_examples(request):
	return render_to_response('apiexamples/apiexamples.html')