
function validate_csv()
{
    file_name = document.getElementById("fileinput").value;
    if( file_name.substr(file_name.length - 4) == '.csv')
    {
              $( "#form_validate" ).submit();
    }
    else
    {
         alert("please select proper input file ")
         $( "#fileinput" ).focus();
    }
}

function selectedvalue(id)
{
      var result = confirm("Are you sure you wish to delete this "  + id + " id?");
      if (result)
      {
            window.location.href = "/delete_record/" + id;
      }
}