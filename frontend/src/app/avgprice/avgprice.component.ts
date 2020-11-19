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
    this.globalAverage = this.API.getGlobalAverage();
  }

}
