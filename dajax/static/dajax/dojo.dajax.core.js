var Dajax = {
    process: function(data)
    {
        dojo.forEach(data, function(elem,i){
        switch(elem.cmd)
        {
            case 'alert':
                alert(elem.val);
            break;

            case 'data':
                eval( elem.fun+"(elem.val);" );
            break;

            case 'as':
                if(elem.prop === 'innerHTML'){
                    dojo.forEach(dojo.query(elem.id), function(e){
                        require(["dojo/html"], function(html){
                            html.set(e, elem.val);
                        });
                    });
                }
                else{
                    dojo.forEach(dojo.query(elem.id),function(e){ e[elem.prop] = elem.val; });
                }
            break;

            case 'addcc':
                dojo.forEach(elem.val,function(e){
                    dojo.query(elem.id).addClass(e);
                });
            break;

            case 'remcc':
                dojo.forEach(elem.val,function(e){
                    dojo.query(elem.id).removeClass(e);
                });
            break;

            case 'ap':
                dojo.forEach(dojo.query(elem.id),function(e){ e[elem.prop] += elem.val;});
            break;

            case 'pp':
                dojo.forEach(dojo.query(elem.id),function(e){ e[elem.prop] = elem.val + e[elem.prop] ;});
            break;

            case 'clr':
                dojo.forEach(dojo.query(elem.id),function(e){ e[elem.prop] = ""; });
            break;

            case 'red':
                window.setTimeout('window.location="'+elem.url+'";',elem.delay);
            break;

            case 'js':
                eval(elem.val);
            break;

            case 'rm':
                dojo.forEach(dojo.query(elem.id), "dojo.query(item).orphan();");
            break;

            default:
            break;
            }
        });
    }
};
