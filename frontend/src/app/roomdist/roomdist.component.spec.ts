import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RoomdistComponent } from './roomdist.component';

describe('RoomdistComponent', () => {
  let component: RoomdistComponent;
  let fixture: ComponentFixture<RoomdistComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RoomdistComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RoomdistComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
