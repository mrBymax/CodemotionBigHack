function loadComponentsInside(name, where){
    fetch(`http://localhost:8083/v1/classify/getInfo/${name}`, {
                    method: "GET",
                    mode: 'cors'
                })
                .then(response => response.json())
                .then(data => {
                    let where2 = where.split("#")[1];
                    let html = `<div id="accordion">`;
                    
                    for(let i in data){
                        let component = data[i];
                        html += `
                        <div class="card">
<div class="card-header2" id="heading${where2}${i}">
<h5 class="mb-0">
<button class="btn btn-link" data-toggle="collapse" 
data-target="#component${where2}${i}" 
aria-expanded="true" 
aria-controls="collapseOne">
${component.name}
</button>
</h5>
</div>

<div id="component${where2}${i}" class="collapse" aria-labelledby="heading${where2}${i}" data-parent="#accordion">
<div class="card-body">
${component.description}
</div>
</div>
</div>
                        `
                        console.log(component)
                    }
                    html += "</div>"; 


                    $(where+" #componentList").html(html);
    });
}


function showDataForDevice(item, where) {
    let name = item.class,
        imgUrl = item.imgEndpoint;

    let html =  `<h1 class="marginTop">${name.toUpperCase()}</h1>` +
                `<div class="alignCenter"><img src="${imgUrl}" alt="No block diagram available" /></div>` +
                `<br />`+
                `<h1>ST components inside:</h1>` +
                `<div id="componentList">Loading...</div>`;
    
    $(where).html(html);

    loadComponentsInside(name, where);
}