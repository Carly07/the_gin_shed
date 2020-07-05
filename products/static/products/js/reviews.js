

const starRating=document.querySelector(".stars").children;
const ratingValue=document.querySelector("#rating-value");
    let index;

    for(let i=0; i<starRating.length; i++){
        starRating[i].addEventListener("mouseover",function(){
            //console.log(i)
            for (let j=0; j<=starRating.length; j++){
                starRating[j].classList.remove("fas fa-star");
                starRating[j].classList.add("far fa-star");
            }
            for (let j=0; j<=i; j++){
                starRating[j].classList.remove("far fa-star");
                starRating[j].classList.add("fas fa-star");
            }
        });
        starRating[i].addEventListener("click",function(){
            ratingValue.value=i+1;
            index=i;
        });
        starRating[i].addEventListener("mouseout",function(){
            //console.log(i)
            for(let j=0; j<=starRating.length; j++){
                starRating[j].classList.remove("fas fa-star");
                starRating[j].classList.add("far fa-star");
            }
            for(let j=0; j<=index; j++){
                starRating[j].classList.remove("far fa-star");
               starRating[j].classList.add("fas fa-star");
            }
        });
    }
