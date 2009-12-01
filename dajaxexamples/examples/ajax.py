from dajax.core import Dajax
	
def request_points(request):
	dajax = Dajax()
	
	points = []
	points.append({'lat':37.41444798751896,'lng':-122.0916223526001,'text':'Some Site #1'})
	points.append({'lat':37.412061929307924,'lng':-122.08582878112793,'text':'Other Site #2'})
	points.append({'lat':37.41301636171327,'lng':-122.0780611038208,'text':'Other Site #3'})
	
	dajax.addData(points,'example_draw_points')
	dajax.assign('#example_log','value',"3 Points loaded...")
	return dajax.json()
	
def move_point(request):
	dajax = Dajax()
	message = "Saved new location at, %s, %s" % (request.POST['lat'],request.POST['lng'])
	dajax.assign('#example_log','value',message)
	return dajax.json()
	
def multiply(request):
	dajax = Dajax()
	result = int(request.POST['a']) * int(request.POST['b'])
	dajax.assign('#result','value',str(result))
	return dajax.json()

def randomize(request):
	import random
	dajax = Dajax()
	dajax.assign('#result','value',random.randint(1, 10))
	return dajax.json()

def updatecombo(request):
	dajax = Dajax()
	options = [ ['Madrid','Barcelona','Vitoria','Burgos'],
				['Paris','Evreux','Le Havre','Reims'],
				['London','Birmingham','Bristol','Cardiff'],]
	out = ""
	for o in options[int(request.POST['option'])]:
		out = '%s<option value="#">%s</option>' % (out,o,)
		
	dajax.assign('#combo2','innerHTML',out)
	return dajax.json()

def pagination(request):
	from dajaxexamples.examples.views import get_pagination_page
	from django.template.loader import render_to_string
	try:
		page = int( request.POST['p'] )
	except:
		page = 1
	items = get_pagination_page(page)
	render = render_to_string('examples/pagination_page.html', { 'items': items })
	
	dajax = Dajax()
	dajax.assign('#pagination','innerHTML',render)
	return dajax.json()

def send_form(request):
	from dajaxice.utils import deserialize_form
	from forms import ExampleForm
	
	dajax = Dajax()
	form_data = deserialize_form( request.POST.get('form') )
	form = ExampleForm(form_data)
	
	if form.is_valid():
		dajax.removeCSSClass('#my_form input','error')
		dajax.alert("This form is_valid(), your username is: %s" % form.cleaned_data.get('username'))
	else:
		dajax.removeCSSClass('#my_form input','error')
		for error in form.errors:
			dajax.addCSSClass('#id_%s' % error,'error')
	return dajax.json()

def flickr_save(request):
	dajax = Dajax()
	new_title = request.POST.get('new_title')
	# Use new_title...
	dajax.script('cancel_edit();')
	dajax.assign('#title','value',new_title)
	dajax.alert('Save complete using "%s"' % new_title )
	return dajax.json()