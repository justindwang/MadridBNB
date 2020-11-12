import { Component, OnInit } from '@angular/core';
import { count } from 'console';
import { ApiCallService } from '../api-call.service';

@Component({
  selector: 'app-roomdist',
  templateUrl: './roomdist.component.html',
  styleUrls: ['./roomdist.component.css']
})
export class RoomdistComponent implements OnInit {
  room_dist_data; 

  constructor(private API : ApiCallService, ) {

  }

  ngOnInit() {
    this.makeEnter();
    
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

            for (let r of this.room_dist_data) {
              r.total = r.entire_count + r.hotel_count + r.private_count + r.shared_count;
              r.e_p = Math.trunc(r.entire_count / r.total * 100);
              r.h_p = Math.trunc(r.hotel_count / r.total * 100);
              r.p_p = Math.trunc(r.private_count / r.total * 100);
              r.s_p = Math.trunc(r.shared_count / r.total * 100);
            }

            console.log("Valid Reponse");
            //console.log(response);
          } else { //invalid response
            console.log("Invalid Response");
          }
        }
      );
  }

}
