$("#get-cus-data").click(function(e){
    e.preventDefault();
    $nationalid = $('#customerdata').val();
    $.ajax({
        url:"",
        dataType:"json",
        type:"post",
        data:{
            nationalid : $nationalid,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        
        success:function(data){
            $('#sub_category_name').html(data['details'][0]['fields'].sub_category_name)
            $('#category_name').html(data['details'][0]['fields'].category_name)
            $('#client_name_m').html(data['details'][0]['fields'].client_name_m)
            $('#inst').html(data['details'][0]['fields'].inst)
            $('#loan_am').html(data['details'][0]['fields'].loan_am)
            $('#aprv_no').html(data['details'][0]['fields'].aprv_no)
            $('#loan_date').html(data['details'][0]['fields'].loan_date)
            $('#aprv_am').html(data['customer'][0]['fields'].aprv_am)
            $('#officer_name').html(data['customer'][0]['fields'].officer_name) 
            $('#tel4').html(data['customer'][0]['fields'].tel4)
            $('#id').html(data['customer'][0].pk)
            $('#consumer_finance_initial_limit').html(data['customer'][0]['fields'].consumer_finance_initial_limit)
            $('#branch_name').html(data['customer'][0]['fields'].branch_name)
            $('#client_key').html(data['customer'][0]['fields'].client_key)
            $('#client_name').html(data['customer'][0]['fields'].client_name)
            $('#client_keyd').html(data['damen'][0]['fields'].client_key)
            $('#client_named').html(data['damen'][0]['fields'].client_name)
            $('#add4d').html(data['damen'][0]['fields'].add4)
            $('#tel4d').html(data['damen'][0]['fields'].tel4)
            $('#ntid').html(data['damen'][0].pk)
            $('#client_keydd').html(data['damen'][1]['fields'].client_key)
            $('#client_namedd').html(data['damen'][1]['fields'].client_name)
            $('#add4dd').html(data['damen'][1]['fields'].add4)
            $('#tel4dd').html(data['damen'][1]['fields'].tel4)
            $('#ntidd').html(data['damen'][1].pk)
            if(data['damen'][1]['fields'].client_key != null){
                $('#client_keydd').html(data['damen'][1]['fields'].client_key)
                $('#client_namedd').html(data['damen'][1]['fields'].client_name)
                $('#add4dd').html(data['damen'][1]['fields'].add4)
                $('#tel4dd').html(data['damen'][1]['fields'].tel4)
                $('#ntidd').html(data['damen'][1].pk)
            }else{
                $('#client_keydd').html('--')
                $('#client_namedd').html('--')
                $('#add4dd').html('--')
                $('#tel4dd').html('--')
                $('#ntidd').html('--') 
            }
        },
        error:function(e){
            alert('There Is An Error')
        },
        complete:function(){}
    })
})





$("#submitting").click(function(e) {
    e.preventDefault();



});
$("#mycheckbox1").change(function() {
$("#mycheckboxdiv1").toggle();


});
$("#mycheckbox2").change(function() {
$("#mycheckboxdiv2").toggle();


});
$("#mycheckbox3").change(function() {
$("#mycheckboxdiv3").toggle();


});
$("#mycheckbox4").change(function() {
$("#mycheckboxdiv4").toggle();


});
$("#mycheckbox5").change(function() {
$("#mycheckboxdiv5").toggle();


});
$("#mycheckbox6").change(function() {
$("#mycheckboxdiv6").toggle();


});
$("#mycheckbox7").change(function() {
$("#mycheckboxdiv7").toggle();


});
$("#mycheckbox8").change(function() {
$("#mycheckboxdiv8").toggle();


});
$("#mycheckbox9").change(function() {
$("#mycheckboxdiv9").toggle();


});
$("#mycheckbox10").change(function() {
$("#mycheckboxdiv10").toggle();


});
$("#mycheckbox11").change(function() {
$("#mycheckboxdiv11").toggle();


});
$("#mycheckbox12").change(function() {
$("#mycheckboxdiv12").toggle();


});
$("#mycheckbox13").change(function() {
$("#mycheckboxdiv13").toggle();


});
$("#mycheckbox14").change(function() {
$("#mycheckboxdiv14").toggle();


});
$("#mycheckbox15").change(function() {
$("#mycheckboxdiv15").toggle();


});
$("#mycheckbox16").change(function() {
$("#mycheckboxdiv16").toggle();


});
$("#mycheckbox17").change(function() {
$("#mycheckboxdiv17").toggle();


});
$("#rad1").change(function() {

$("#rado").toggle();


});