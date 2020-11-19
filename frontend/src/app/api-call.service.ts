import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiCallService {

  globalAverage;

  constructor(
    private http: HttpClient
  ) { }

  getGlobalAverage(){
    return this.globalAverage;
  }

  getListings(searchData){
    //returns listing data based on inputted searchData
    /*searchData = {
      "neighborhood" : None,
      "roomType" : None,
      "priceRange" : [0,100]
    }
    */
    return this.http.post<any>('http://127.0.0.1:5000/listings', searchData);
  }

  addListing(listingData){
    return this.http.post<any>('http://127.0.0.1:5000/listings/add', listingData);
  }

  removeListing(listingData){
    return this.http.post<any>('http://127.0.0.1:5000/listings/remove', listingData);
  }

  editListing(listingData){
    return this.http.post<any>('http://127.0.0.1:5000/listings/edit', listingData);
  }

  getReviews(searchData){
    //returns review data based on inputted searchData
    /*searchData = {
      "dateRange" : [],
      "reviewerName" : "Name"
    */
    return this.http.post<any>('http://127.0.0.1:5000/reviews', searchData);
  }

  getNeighborhoods(searchData){
     //returns neighborhood data based on inputted searchData
    /*searchData = {
      "neighborhoodName" : "Name",
      "neighboorhoodGroup" : "Name"
    */
    return this.http.post<any>('http://127.0.0.1:5000/neighborhoods', searchData);
  }

  getAnalytics(){
    //returns neighborhood data based on inputted searchData
   /*searchData = {
     "neighborhoodName" : "Name",
     "neighboorhoodGroup" : "Name"
   */
  let response = this.http.get<any>('http://127.0.0.1:5000/analytics');
  this.globalAverage = response['global_average'];
  return response;
 }

}
