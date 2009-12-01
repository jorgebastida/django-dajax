from dajax.core import Dajax
from django.template.loader import render_to_string
	
def assign_test(request):
	dajax = Dajax()
	dajax.assign('#block01 li','innerHTML','Something else...')
	dajax.append('#console','innerHTML',"dajax.assign('#block01 li','innerHTML','Something else...')<br/>")
	return dajax.render()
		
def clear_test(request):
	dajax = Dajax()
	dajax.clear('#block02 li','innerHTML')
	dajax.append('#console','innerHTML',"dajax.clear('#block02 li','innerHTML')<br/>")
	return dajax.render()

def alert_test(request):
	dajax = Dajax()
	dajax.alert('Alert Test Works!!')
	dajax.append('#console','innerHTML',"dajax.alert('Alert Test Works!!')<br/>")
	return dajax.render()
	
def cssadd_test(request):
	dajax = Dajax()
	dajax.addCSSClass('#block04 li',('red',))
	dajax.append('#console','innerHTML',"dajax.addCSSClass('#block04 li',('red',))<br/>")
	return dajax.render()
	
def cssrem_test(request):
	dajax = Dajax()
	dajax.removeCSSClass('#block04 li',('red',))
	dajax.append('#console','innerHTML',"dajax.removeCSSClass('#block04 li',('red',))<br/>")
	return dajax.render()

def append_test(request):
	dajax = Dajax()
	dajax.append('#block06 .row','innerHTML','#')
	dajax.append('#console','innerHTML',"dajax.append('#block06 .row','innerHTML','#')<br/>")
	return dajax.render()

def prepend_test(request):
	dajax = Dajax()
	dajax.prepend('#block07 .row','innerHTML','#')
	dajax.append('#console','innerHTML',"dajax.prepend('#block07 .row','innerHTML','#')<br/>")
	return dajax.render()

def redirect_test(request):
	dajax = Dajax()
	dajax.redirect('http://djangoproject.com',2000)
	dajax.append('#console','innerHTML',"dajax.redirect('http://djangoproject.com',2000)<br/>")
	return dajax.render()

def script_test(request):
	dajax = Dajax()
	dajax.script('alert("Alert from script!")')
	dajax.append('#console','innerHTML',"dajax.script('alert(\'Alert from script!\')')<br/>")
	return dajax.render()
	
def remove_test(request):
	dajax = Dajax()
	dajax.remove('#block10 .row')
	dajax.append('#console','innerHTML',"dajax.remove('#block10 .row')<br/>")
	return dajax.render()

def adddata_test(request):
	dajax = Dajax()
	dajax.addData(range(0,10),'my_callback')
	dajax.append('#console','innerHTML',"dajax.addData(range(0,10),'my_callback')<br/>")
	return dajax.render()
	
def param_test(request):
	dajax = Dajax()
	dajax.alert("You search = "+request.POST['what'])
	dajax.append('#console','innerHTML',"dajax.alert(\'You search = \'+request.POST['what'])<br/>")
	return dajax.render()