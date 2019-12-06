{% block js %}
    <script>
        $(document).ready(function(){
            var siteForm= $(".formulario_crear_site");

            siteForm.submit(function(event){
                event.preventDefault();
                var thisForm = $(this);
                var actionEndpoint =thisForm.attr("action");
                var httpMethod = thisForm.attr("method");
                var formData = thisForm.serialize();


         

            $.ajax({
                url: actionEndpoint,
                method: httpMethod,
                data: formData,
                success: function(data){
                    console.log("success");
                    console.log(data);
                    alert("Proceso completado")
                },
                error: function(errorData){
                    console.log("error");
                    console.log(errorData);
                },
            });
            
            });

           
        });
    </script>
{% endblock js %}