import { Component, OnInit } from '@angular/core';
import { ApiCallService } from '../api-call.service';

import Chart from 'chart.js';

@Component({
  selector: 'app-roomdist',
  templateUrl: './roomdist.component.html',
  styleUrls: ['./roomdist.component.css']
})
export class RoomdistComponent implements OnInit{
  room_dist_data = undefined; 
  madrid_room: boolean = false;
  neighborhood_room: boolean = false;

  constructor(private API : ApiCallService, ) {

  }

  ngOnInit() {
    this.makeEnter();
    
  }

  displayCharts(){
    if (this.room_dist_data != undefined){ //check if room_dist_data is undefined
      for (let i = 0; i < this.room_dist_data.length; i++) {
        let r = this.room_dist_data[i];
        let canvas = document.getElementById('chart_' + i.toString() );
        //console.log(canvas);
        if (canvas != undefined) {
          r.chart = new Chart( canvas,
            {
              type: 'pie',
              data: {
                datasets: [
                  {
                    data: [r.entire_count, r.hotel_count, r.private_count, r.shared_count],
                    backgroundColor: [
                      'rgba(255,255,255,1)',
                      'rgba(255,0,0,1)',
                      'rgba(0,255,0,1)',
                      'rgba(0,0,255,1)',
                    ],
                    borderWidth: 0
                  }
                ],
                labels : ['Entire Home / Appartment', 'Hotel', 'Private Room', 'Shared Room'],
              },
            }
          );
        } else {
          console.log('canvas undefined');
        }
        

        r.total = r.entire_count + r.hotel_count + r.private_count + r.shared_count;
        r.e_p = Math.trunc(r.entire_count / r.total * 100);
        r.h_p = Math.trunc(r.hotel_count / r.total * 100);
        r.p_p = Math.trunc(r.private_count / r.total * 100);
        r.s_p = Math.trunc(r.shared_count / r.total * 100);
      }
    } 
  }

  madridroom_display(){
    let room = document.getElementById('madrid_room');
    if (room.style.display == "none"){
      room.style.display = "block";
    } else {
      room.style.display = "none";
    }
    
   
  }

  neighborhoodroom_display(){
    let room = document.getElementById('neighborhood_room');
    if (room.style.display == "none"){
      room.style.display = "block";
    } else {
      room.style.display = "none";
    }
    
  }


  
  //sends a get request to the server
  makeEnter(){
    console.log("Sending request");
    console.log();

    let response = undefined; //this should be a list of listings objects
    this.API.getAnalytics() //make the API call
      .subscribe( //this runs when the get request gets a response
        (result) => {
          response = result;
        }
      ).add( //this runs after the post reponse has been recieved
        () => {
          if (response != undefined){ //valid response
            console.log(response);
            this.room_dist_data = response.room_dist_data;

            this.displayCharts();
            
            console.log("Valid Reponse");
            //console.log(response);
          } else { //invalid response
            console.log("Invalid Response");
          }
        }
      );
  }

}
