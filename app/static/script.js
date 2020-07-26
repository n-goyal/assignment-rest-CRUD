
//  api check
// var page = 1;
// function loadIndex(page){
//   return fetch(url='http://127.0.0.1:5000/universities/'+page, {
//     method: 'GET',
//     crossOrigin: null,
//     headers: {
//       contentType: 'application/json; charset=utf-8'
//     }
//   })
//   .then(res => res.json())
//   .then(data=>{
//     console.log(data);
//   })
// }

// console.log(loadIndex(page).pages);

fetch(url='http://127.0.0.1:5000/universities/2', {
  method: 'GET',
  crossOrigin: null,
  headers: {
    contentType: 'application/json; charset=utf-8'
  }
})
  .then(res => res.json())
  .then(data => {
    // fetch university data

    // index page
    /*
    div => table => tbody => tr => th => td

    <tr>
      <th scope="row">1</th>
      <td>Abilene Christian University</td>
      <td>United States</td>
      <td>acu.org.us</td>
      <td>acu.edu</td>
      <td>US</td>
      <td class="btn-col">
        <button type="button" class="btn btn-outline-danger">update</button>
      </td> <!--update modal -->
      <td class="btn-col">
        <button type="button" class="btn btn-outline-danger">delete</button>
      </td>
    </tr>
    */
    console.log(data);
    renderTable(data.universities);
    // render pagination

    
})

function renderTable(data){
  var tableBody = document.getElementById('table-body');
  console.log(tableBody);
  for (var i = 1; i <= data.length; i++) {
      // create a row head
      var th = document.createElement('th', scope="row");
      // add value to it
      th.appendChild(document.createTextNode(i));
      // create row data
      /*
          Template: 

          "alpha_two_code": "US",
          "country": "United States",
          "domain": "acu.edu",
          "name": "Abilene Christian University",
          "web_page": "acu.edu.us"

          Table Header:

          <th scope="col">University Name</th>
          <th scope="col">Country</th>
          <th scope="col">Website</th>
          <th scope="col">Domain</th>
          <th scope="col">Code</th>
          <th scope="col">Update</th>
          <th scope="col">Delete</th>
          */
      for(var key in data[i]) {
        var val = data[i][key];
        console.log(val);
        switch(key){
        }
        console.log(key)
      }
      // add value to it
      
      var tr = document.createElement('tr');
      tr.appendChild(th);
      tr.appendChild(document.createElement('td'));
      tr.appendChild(document.createElement('td'));
      tr.appendChild(document.createElement('td'));
      tr.appendChild(document.createElement('td'));
      tr.appendChild(document.createElement('td'));
      var buttons = ['Update', 'Delete']
      
      var btn = document.createElement('button');
      btn.className = "btn btn-outline-danger";
      btn.type=  "button";
      btn.appendChild(document.createTextNode(buttons[0]))
      var td = document.createElement('td');
      td.appendChild(btn);
      tr.appendChild(td);
      
      var btn = document.createElement('button');
      btn.className = "btn btn-outline-danger";
      btn.type=  "button";
      btn.appendChild(document.createTextNode(buttons[1]))
      var td = document.createElement('td');
      td.appendChild(btn);
      tr.appendChild(td);

      tableBody.appendChild(tr);
  }
  console.log(tableBody);
  return tableBody
}



// tablearea.appendChild(table);
