const name_files = document.getElementById("name_filehide").value;
var table_datass = document.querySelector(".table_datas");
var row_show = document.querySelector(".data_java");
var name_buton_analisis = "";
var column_namess ="";
var tbdy = document.createElement('tbody');
var thead = document.createElement('thead');
var tbl = document.createElement("table");
tbl.classList.add("customers")
tbl.id="utama_table"

var path = window.location.pathname;
var page = path.split("/").pop();

if(page == 'upload'){
   get_button_analisis = document.querySelectorAll(".button_anlic");
//   var tableElements = document.getElementsByClassName("button_anlic");
   get_button_analisis.forEach(function(element){
        element.addEventListener('click',function(e){
            var id_analis = e["target"].id;
//            console.log(e["target"].id)
                if(id_analis === 'select_columns'){
                    select_th();
                }else if(id_analis === 'delete_columns'){
                    column_namess=""
                    name_buton_analisis ="delete_columns"
                    column_namess = print_checkbox()
                }else if(id_analis === 'grouping_Data'){
                    column_namess=""
                    name_buton_analisis ="reverse_data"
                }else if(id_analis === 'btn_analisis'){
                    name_buton_analisis ="describe_data"
                    column_namess = print_checkbox();
                }else if(id_analis === 'btn_barplot'){
                    name_buton_analisis ="barplot_data";
                    var data_java = document.querySelector(".data_java");
                    var div_bar = document.createElement('div');
                    div_bar.classList.add('bar_svg')
                    div_bar.style.marginTop = "50px";
                    data_java.append(div_bar)

                    column_namess=print_checkbox()
                }
                else if(id_analis === 'get_before_data'){
                    console.log(e["target"].id)

                }

        });
   });

}

function Alert_error(message){
    alert(message)
}


async function getData(url_data){
    let urls_datas = "http://127.0.0.1:8000/service/render-json/"+url_data+"/";
    try{
        let res = await fetch(urls_datas);
        return await res.json();
    }catch(error){
        console.log(error);
    }
}

function create_judul(name_,margin_){
    var jul_span = document.createElement("span");
    jul_span.innerText = name_.replaceAll("_"," ")
    jul_span.style.fontWeight = "Bold";
    jul_span.style.marginLeft=margin_+"%"
    return jul_span
}


async function renderDatas(){
    if(name_files != ""){
        let datass = await getData(name_files);
        table_datass.append(create_judul(name_files,50));
        let header_col = []
        var tr = document.createElement("tr");
        Object.keys(datass.data[0]).forEach( it =>{
           var th = document.createElement("th");
           th.appendChild(document.createTextNode(it))
           tr.appendChild(th)
        })
        thead.appendChild(tr);
        tbl.appendChild(thead);
        let i=0;
        datass.data.forEach(items =>{
            if(i>=10){
                return false; //for end looping each
            }
            var tr = document.createElement("tr");
            Object.values(items).forEach(chilss =>{
                var td = document.createElement("td");
                td.appendChild(document.createTextNode(chilss))
                tr.appendChild(td)
            });
            tbdy.appendChild(tr);
            i+=1;
        })
        tbl.appendChild(tbdy);
        table_datass.append(tbl);
        document.head.appendChild(Load_css());
    }else{
        console.log("Kosong")
    }


}

function Load_css(){
    var css = document.createElement("link");
    css.rel = "stylesheet";
    css.type="text/css";
    css.id = "table";
    css.href = "/static/css/tabless.css";
    return css
}
renderDatas()

/*select th */

function select_th(){
    name_buton_analisis="select_columns"
    var th_table = document.getElementById("utama_table").querySelectorAll("th");
    if(th_table[0].children.length === 0){
        th_table.forEach(th =>{
            const name_id = th.innerHTML.trim().replaceAll(" ","_");
            var check_th = document.createElement("input")
            check_th.setAttribute("type","checkbox");
            check_th.style.position="relative";
            check_th.style.float ="right";
            check_th.style.marginLeft="0px";
            check_th.classList.add("tble_check");
            check_th.setAttribute("id",name_id);
            th.appendChild(check_th)
        })
    }

}

function print_checkbox(){
    var ex_col ="";
    var ch_table = document.querySelectorAll(".tble_check");
    ch_table.forEach(ch=>{
        if(ch.checked === true){
            ex_col += ch.id+","
        }
    })
    return ex_col
}


$(document).on('submit',"#form_analisis", function(e){
    e.preventDefault();
    $.ajax({
        type:'POST',
        url:'check_data',
        data:
            {
                name_filehide:name_files,
                flag_button:name_buton_analisis,
                column_names:column_namess,
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
        success:function(data){
            console.log(data);
            if(name_buton_analisis === "delete_columns"){
                console.log(data)
                console.log("satu")
                create_table(data)
            }else if(name_buton_analisis === "describe_data"){
                console.log("dua")
                show_describing_data(data)
                console.log("masuk sini")
            }else if(name_buton_analisis === "barplot_data"){
                console.log("tiga")
                barplot_data_detail(data);
            }if(name_buton_analisis === "reverse_data"){
                create_table(data)
            }

        }
    })
});

function barplot_data_detail(datas){
    var width_=1050,height_=400,barwidth = width_ /200;
    var svgContainer = d3.select('.bar_svg').append('svg').attr('width',width_+100).attr('height',height_+60);
    /*After all x and y axis have done, then make a title*/
    svgContainer.append('text')
    .attr('x',-250).style("z-index", 10)
    .attr('y',15)
    .text('Bagian y terakhir dibuat bedasarkan').attr('transform','rotate(-90)')


    var x_axis = d3.scaleBand().range([0,width_]).domain(datas.data.map(function(d){ return d['YearsExperience']}));

    svgContainer.append('g').attr("transform", "translate(70," + height_ + ")").attr('class','x-axis').call(d3.axisBottom(x_axis));
    var salery_dg = datas.data.map(function(d){
        return d['Salary'];
    })
    console.log(document.querySelectorAll('.x-axis'))
    console.log('Panjang :' +datas.data.length)
    console.log(x_axis(1.3));
    max_salary = d3.max(salery_dg);

    var y_axis = d3.scaleLinear().domain([0,max_salary]).range([height_,0]);
    var Y_ = d3.axisLeft(y_axis);
    svgContainer.append('g').attr("transform","translate(70,0)").call(Y_);
    var linearScale = d3.scaleLinear().domain([0, max_salary]).range([0, height_]);
    dat_select = salery_dg.map(function(d){
        return linearScale(d);
    })


    const tooltip = d3.select('.bar_svg').append('div')
    .attr('class', 'd3-tooltip')
    .style('position', 'absolute')
    .style('z-index', '10')
    .style('visibility', 'hidden')
    .style('padding', '10px')
    .style('background', 'rgba(0,0,0,0.6)')
    .style('border-radius', '4px')
    .style('color', '#fff')
    .text('a simple tooltip');


    /* For create a rect */
    svgContainer.selectAll("rect")
    .data(dat_select).enter()
    .append("rect").attr('class','bar')
    .attr('x',function(d,i){
        console.log(x_axis(datas.data[i].YearsExperience))
        if(i===0){
            return x_axis(datas.data[i].YearsExperience)+78;
        }else{
            return x_axis(datas.data[i].YearsExperience)+78;
        }
    })
    .attr('y',function(d,i){ return height_-d; })
    .attr('width','20px')
    .attr('height',function(d){return d;})
    .on('mouseover', function (d, i) {
          tooltip
            .html(
              `<div>YearsExperience : ${datas.data[i]['YearsExperience']}</div><div>Salary : ${datas.data[i]['Salary']}</div>`
            )
            .style('visibility', 'visible');
      })
      .on("mousemove", function(){return tooltip.style("top", (d3.event.pageY-10)+"px").style("left",(d3.event.pageX+10)+"px");})
      .on('mouseout',()=>{tooltip.style("visibility","hidden")});
}



function create_table(datass){
    tbl.innerHTML = "";
    tbdy.innerHTML="";
    thead.innerHTML ="";
    var tr = document.createElement("tr");
    var list_head = Object.keys(datass.data[0])
    if(name_buton_analisis == "reverse_data"){
        list_head = Object.keys(datass.data[0]).reverse();
        console.log(list_head)
    }

//    Object.keys(datass.data[0])
    list_head.forEach( it =>{
           var th = document.createElement("th");
           th.appendChild(document.createTextNode(it))
           tr.appendChild(th)
    })
    thead.appendChild(tr);
    tbl.appendChild(thead);
    let i=0;
    datass.data.forEach(items =>{
        if(i>=10){
            return false; //for end looping each
        }
        var tr = document.createElement("tr");
        var list_values = Object.values(items)
        if(name_buton_analisis == "reverse_data"){
            list_values = Object.values(items).reverse();
        }
        console.log(list_values)
        list_values.forEach(chilss =>{
            var td = document.createElement("td");
            td.appendChild(document.createTextNode(chilss))
            tr.appendChild(td)
        });
        tbdy.appendChild(tr);
        i+=1;
    })
    tbl.appendChild(tbdy);
    table_datass.append(tbl);
    document.head.appendChild(Load_css());
    let height_tbl = document.querySelector(".data_java").offsetHeight = document.querySelector(".data_java").offsetHeight+50;
    document.querySelector(".data_java").style.height = height_tbl+ "px";
}



function show_describing_data(datass){
    describe_data_div = document.querySelector(".describing_datas");
    describe_data_div.innerHTML ="";
    describe_data_div.append(create_judul("Describe_Data_Of_"+name_files,40))
    describe_data_div.append(add_panah("desc_panah"))
    describe_data_div.style.marginTop="70px";
    D_tbdy = document.createElement('tbody');
    D_thead = document.createElement('thead');
    D_tbl = document.createElement("table");
    D_tbl.id = name_buton_analisis;
    var tr = document.createElement("tr");
    D_tbl.classList.add("customers");
    for(let i=0;i<datass.list_columns.length+1;i++){
        var th = document.createElement("th");
        var col_name = datass.list_columns[i-1];
        if(i==0){
            col_name = "";
        }
        th.appendChild(document.createTextNode(col_name));
        tr.appendChild(th);
    }
    D_thead.appendChild(tr);
    D_tbl.appendChild(D_thead);
    list_desc_col = ["count","mean","std","min","25%","50%","75%","max"]
    list_desc_col.forEach(ldc =>{
        tr = document.createElement("tr");
        var td = document.createElement("td");
        td.appendChild(document.createTextNode(ldc))
        tr.appendChild(td)
        datass.list_columns.forEach(lc =>{
             td = document.createElement("td");
             td.appendChild(document.createTextNode(datass.data[lc][ldc]))
             tr.appendChild(td)
        })
        D_tbdy.appendChild(tr);
    })
    D_tbl.appendChild(D_tbdy);
    describe_data_div.append(D_tbl);
}


function add_panah(id_panah){
    var div_panah = document.createElement("div");
    div_panah.setAttribute("onclick","flip_panah(this.id)")
    div_panah.id = "dec_flip"
    var hr_ = document.createElement("hr")
    hr_.style.width ="99,5%";
    hr_.style.marginLeft="10px"
    hr_.style.marginTop="-12px"
    var span_ = document.createElement("span")
    span_.classList.add("dec_flip")
    span_.innerText = "+"
    div_panah.style.cursor ="pointer";
    span_.appendChild(hr_)
    div_panah.append(span_);

    return div_panah;
}



function flip_panah(id_panah){
    var hr_ = document.createElement("hr")
    hr_.style.width ="99,5%";
    hr_.style.marginLeft="10px"
    if(document.querySelector("."+id_panah).innerText == "-"){
        document.querySelector("."+id_panah).innerText = "+"
        hr_.style.marginTop="-12px"
        if(id_panah =="dec_flip"){
            document.getElementById("describe_data").classList.remove("hidden");
        }
    }else{
        document.querySelector("."+id_panah).innerText ="-";
        hr_.style.marginTop="-10px"
        if(id_panah =="dec_flip"){
            document.getElementById("describe_data").classList.add("hidden");
        }
    }
    document.querySelector("."+id_panah).appendChild(hr_)

}