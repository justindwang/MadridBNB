import { Component, OnInit } from '@angular/core';
import { ApiCallService } from '../api-call.service';

@Component({
  selector: 'app-avgprice',
  templateUrl: './avgprice.component.html',
  styleUrls: ['./avgprice.component.css']
})
export class AvgpriceComponent implements OnInit {
  globalAverage;

  constructor( private API : ApiCallService,) { }

  ngOnInit() {
    

    let response = undefined;
    this.API.getAnalytics() //make the API call
      .subscribe( //this runs when the get request gets a response
        (result) => {
          response = result;
        }
      ).add( //this runs after the post reponse has been recieved
        () => {
          if (response != undefined){ //valid response
            console.log(response);
            
            this.globalAverage = response.global_average;
            
            console.log("Valid Reponse");
            //console.log(response);
          } else { //invalid response
            console.log("Invalid Response");
          }
        }
      );
  }

}
