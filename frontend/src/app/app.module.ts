import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { HttpClientModule } from '@angular/common/http';
import { ReactiveFormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { AppRoutingModule, routingComponents } from './app-routing.module';
import { PopularityComponent } from './popularity/popularity.component';
import { RoomdistComponent } from './roomdist/roomdist.component';
import { AvgpriceComponent } from './avgprice/avgprice.component';
import { ReviewsComponent } from './reviews/reviews.component';

@NgModule({
  declarations: [
    AppComponent,
   routingComponents,
   PopularityComponent,
   RoomdistComponent,
   AvgpriceComponent,
   ReviewsComponent


  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    ReactiveFormsModule,
    AppRoutingModule

  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
