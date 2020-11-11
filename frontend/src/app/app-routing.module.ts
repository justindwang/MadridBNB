import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ListingsComponent } from './listings/listings.component'
import { AddlistingComponent } from './addlisting/addlisting.component'
import { EditlistingComponent } from './editlisting/editlisting.component'
import { DeletelistingComponent } from './deletelisting/deletelisting.component'
import { PopularityComponent } from './popularity/popularity.component'

const routes: Routes = [

    {path: 'listings', component: ListingsComponent},
    {path: 'addlisting', component: AddlistingComponent},
    {path: 'editlisting', component: EditlistingComponent},
    {path: 'deletelisting', component: DeletelistingComponent},
    {path: 'popularity', component: PopularityComponent}

];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})

export class AppRoutingModule {}
export const routingComponents = [ListingsComponent, AddlistingComponent,EditlistingComponent,DeletelistingComponent,PopularityComponent]