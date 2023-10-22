.filters {
    background-color: white;
    height: 70px;
    border: 1px solid #575757;
    border-radius: 4px;
    display: flex;  
    align-items: center;
    position: relative;
    
}

.filters button {
    font-size: 18px;
    background-color: #AA0004;
    color: #FFFFFF;
    height: 48px;
    width: 20%;
    border: none;
    border-radius: 4px;
    position: absolute;
    right: 30px;
    box-sizing: border-box;
}
.filters button:hover {
    
    background-color: #223FB0;
}

.filters .locations,.filters .amenities {

    height: 100%; 
    width: 25%;
    position: relative;
    display: flex;
    justify-content: center; 
    flex-direction: column; 
    box-sizing: border-box;
}

.locations {
    border-right: 1px solid  #575757 ;
}

.filters .locations h3,  .filters .amenities h3{
    font-weight: 600;
    margin: 2px 20px;
}
.locations h4,  .amenities h4{
    font-weight: 400;
    font-size: 14px;
    margin: 2px 20px;   
    
}
.popover {
    display: none;
    background-color: #FAFAFA;
    border: 1px solid #575757;
    border-radius: 4px;
    position: absolute;
    box-sizing: border-box;
    width: 100%;
    top: 100%;
    margin-top: 0;
}

div:hover > .popover {
    display: block;
    cursor: pointer;
    
  }
.popover h2 {
    font-size: 16px;
}
.popover li {
    margin: 10px 0px 5px 0px; 
    list-style: none;
}

.filters .locations ul {
    padding: 0.5em 0 1em 1em;
  }
  
.filters .locations li {
    margin: 0 0 0 5%;
    padding: 0.2em;
}
.filters .amenities ul {
    padding: 2em 0 2em 3em;
  }


@media only screen and (max-width: 1030px) 
{
    .filters {
        width: 90%;
        margin: 0 auto;
    }
}
@media only screen and (max-width: 600px) 
{
    .filters .locations,.filters .amenities {
        width: 35%;
    }
    .filters .locations ul, .filters .amenities ul  {
        padding: 0.7em;
      }
    .filters .locations li {
        margin: 0 0 0 5%;
        padding: 0;
    }

}
@media only screen and (max-width: 360px) 
{
    .filters button {
        font-size: 16px;
        justify-content: center;
        right: 8px;
        width: 25%;
        padding: 0px;
    }
}
@media only screen and (max-width: 350px) 
{
    .filters .locations,.filters .amenities {
        width: 35%;
        font-size: 0.85em;
    }
    .filters .locations h3,  .filters .amenities h3{
        font-size: 1.1em;
        margin: 2px 7px;
    }
    .locations h4,  .amenities h4{
        font-weight: 400;
        font-size: 0.9em;
        margin: 2px 7px;    
    }
    .filters .locations ul {
        padding: 0.1em;
      }
    .filters .amenities ul {
        padding: 0.8em;

    }
}
@media only screen and (max-width: 280px) 
{
    .filters button {
        font-size: 12px;
        width: 20%;
        padding: 0;
    }
    .popover h2 {
        font-size: 11px;
    }
    .filters .locations ul {
        font-size: 0.9em;
    }
    .filters .amenities ul {
        font-size: 0.9em;
    }
    
}
@media only screen and (max-width: 250px) 
{
    .filters button {
        font-size: 11px;
        width: 20%;
        padding: 0;   
    }
    .filters .locations h3,  .filters .amenities h3{
        font-size: 0.9em;
    }

    .filters .locations ul{
        padding: 0;
      }
    .filters .amenities ul {
        padding: 1em;
    }
}
