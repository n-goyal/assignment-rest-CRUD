
var prevPage, nextPage, currPage, totalPage, searchKey, jsonData;
loadIndex(1);
// init();

// pagination
currPage = 1;
prevPage = 1;
document.getElementById('curr-page').innerHTML = currPage;

var count;

// render table with data and buttons
function renderTable(data){
  var col = [];
        for (var i = 0; i < data.length; i++) {
            for (var key in data[i]) {
                if (col.indexOf(key) === -1) {
                    col.push(key);
                }
            }
        }
        var table = document.createElement("table");
        var tr = table.insertRow(-1);
        // set headers
        var columns = ["id", "Code", "Country", "Domain", "University Name", "Website", "Update", "Delete"]
        for (var i = 0; i < columns.length; i++) {
          var th = document.createElement("th");
          th.innerHTML = columns[i];
          th.style.position = 'sticky';
          tr.appendChild(th);
        }
        for (var i = 0; i < data.length; i++) {
          tr = table.insertRow(-1);
          var id = tr.insertCell(0);
          id.innerHTML = i
          for (var j = 0; j < col.length; j++) {
            var tabCell = tr.insertCell(-1);
            tabCell.innerHTML = data[i][col[j]];
          }
          var cell1 = tr.insertCell(6);
          var cell2 = tr.insertCell(7);
          var buttons = ['Update', 'Delete']
      
          var btn = document.createElement('button');
          btn = document.getElementById('btn-create').cloneNode(true);
          btn.textContent = buttons[0];
          btn.Id = 'btn-update';
          btn.className = "btn btn-outline-success";
          cell1.appendChild(btn);

          var btn2 = document.createElement('button');
          btn2.className = "btn btn-outline-danger";
          btn2.type=  "button";
          btn2.appendChild(document.createTextNode(buttons[1]))
          btn2.Id = buttons[1];
          cell2.appendChild(btn2);
        }
        var divContainer = document.getElementById("showData");
        divContainer.innerHTML = "";
        divContainer.appendChild(table);
}

document.getElementById('btn-prev').addEventListener('click', function(){
  if(currPage != 1){
    // call api with prevPage
    nextPage = currPage;
    prevPage = currPage - 1;
    currPage = prevPage
    loadIndex(prevPage);
    // console.log(prevPage);
    document.querySelector('.btn-next').classList.remove('disabled');
    document.getElementById('curr-page').innerHTML = currPage;
  }
  else{
    // disable the button
    document.getElementById('.btn-prev').classList.add('disabled');
  }
});

document.getElementById('btn-next').addEventListener('click', function(){
  if(currPage != totalPage){
    // call api with nextPage
    nextPage = currPage + 1;
    prePage = currPage;
    currPage = nextPage;
    // console.log(nextPage);
    loadIndex(nextPage);
    document.querySelector('.btn-prev').classList.remove('disabled');
    document.getElementById('curr-page').innerHTML = currPage;
  }
  else{
    // disable the button
    document.querySelector('.btn-next').classList.add('disabled');
  }
});


// search
document.getElementById('btn-search').addEventListener('click', function() {
  searchKey = document.getElementById('search-input').value;
  if (searchKey===""){
    // add bootstrap control error
    console.log('coming as empty');
    loadIndex(1);
  }
  else{
    console.log(searchKey);
    searchUni(searchKey, 1);
  }
})

// update button
document.getElementById()


function loadIndex(page) {
  fetch(url='http://127.0.0.1:5000/universities/'+page, {
    method: 'GET',
    crossOrigin: null,
    headers: {
      contentType: 'application/json; charset=utf-8'
    }
  })
  .then(res => res.json())
  .then(data=>{
    totalPage = data.pages;
    document.getElementById('total-page').innerHTML = totalPage;
    jsonData = data.universities;
    renderTable(data.universities);
    console.log(data.page);
    console.log(data.universities);
  })
}

function searchUni(searchKey, page) {
  currPage = 1;
  totalPage = 1;
  fetch(ulr='http://127.0.0.1:5000/universities/get-details/'+searchKey+'/'+page,{
    method: 'GET',
    crossOrigin: null,
    headers: {
      contentType: 'application/json; charset=utf-8'  
    }
  })
  .then(res => res.json())
  .then(data => {
    totalPage = data.pages;
    jsonData = data.matches;
    renderTable(data.matches);
    console.log(data.totalMatches);
  })
  .then(document.getElementById('total-page').innerHTML = totalPage)
}

function deleteRecord(jsonData, Id) {
  // get university name
  university_name = jsonData[Id + 1]['name']
  // do a delete request
  fetch(url='http://127.0.0.1:5000/' + university_name + '/delete-record/', {
    method: 'DELETE',
    crossOrigin: null,
    headers: {
      contentType: 'application/json; charset=utf-8'  
    }
  })
  // refresh the page
  loadIndex(1);
}

// digest update api
function updateRecord(jsonData, Id) {
  // get university name
  university_name = jsonData[Id + 1]['name']
  // call update api
  fetch(url='http://127.0.0.1:5000/' + university_name + '/udpate/', {
    method: 'PUT',
    // body: get data from modal
    crossOrigin: null,
    headers: {
      contentType: 'application/json; charset=utf-8'
    }
  })
}

// digest create api
function createRecord() {
  // call update api
  fetch(url='http://127.0.0.1:5000/create/', {
    method: 'POST',
    // body: get data from modal
    crossOrigin: null,
    headers: {
      contentType: 'application/json; charset=utf-8'
    }
  })
}
