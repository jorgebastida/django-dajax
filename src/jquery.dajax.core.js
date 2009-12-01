var Dajax = {
    process: function(data)
    {
        $.each(data, function(i,elem){
            switch(elem.cmd)
            {
                case 'alert':
                    alert(elem.val)
                break;
        
                case 'data':
                    eval( elem.fun+"(elem.val);" );
                break;
        
                case 'as':
                    elem.val = clear_quotes(elem.val);
                    jQuery.each($(elem.id),function(){ this[elem.prop] = elem.val; });
                break;
        
                case 'addcc':
                    jQuery.each(elem.val,function(){
                        $(elem.id).addClass(this);
                    });
                break;
            
                case 'remcc':
                    jQuery.each(elem.val,function(){
                        $(elem.id).removeClass(this);
                    });
                break;
            
                case 'ap':
                    jQuery.each($(elem.id),function(){ this[elem.prop] += elem.val; });
                break;
            
                case 'pp':
                    jQuery.each($(elem.id),function(){ this[elem.prop] = elem.val + this[elem.prop]; });
                break;
            
                case 'clr':
                    jQuery.each($(elem.id),function(){ this[elem.prop] = ""; });
                break;
            
                case 'red':
                    window.setTimeout('window.location="'+elem.url+'";',elem.delay);
                break;
            
                case 'js':
                    eval(elem.val);
                break;
            
                case 'rm':
                    $(elem.id).remove();
                break;
            
                default:
                    alert('Unknown action!');
            }
        });
    }
};