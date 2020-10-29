import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DeletelistingComponent } from './deletelisting.component';

describe('DeletelistingComponent', () => {
  let component: DeletelistingComponent;
  let fixture: ComponentFixture<DeletelistingComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DeletelistingComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DeletelistingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
