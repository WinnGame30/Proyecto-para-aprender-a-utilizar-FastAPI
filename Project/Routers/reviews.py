from fastapi import HTTPException
from fastapi import APIRouter

from ..database import User, Videojuego, UserReview
from ..schemas import ReviewRequestModel, ReviewResponseModel, ReviewModificarModel

from typing import List

router = APIRouter(prefix="/reviews")

@router.post("/", response_model=ReviewResponseModel)
async def create_review(new_review: ReviewRequestModel):

    if User.select().where(User.id == new_review.user_id).first() is None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    
    if Videojuego.select().where(Videojuego.id == new_review.videojuego_id).first() is None:
        raise HTTPException(status_code=404, detail="El videojuego no existe")

    review = UserReview.create(user_id = new_review.user_id,
                               videojuego = new_review.videojuego_id,
                               review = new_review.review,
                               score = new_review.score)
    
    return review

@router.get("/", response_model=List[ReviewResponseModel])
async def listado_reviews(page: int = 1, limit : int = 10):
    reviews = UserReview.select().paginate(page, limit)
    return reviews

@router.get("/{id}", response_model=ReviewResponseModel)
async def review_particular(id: int):
    review = UserReview.select().where(UserReview.id == id).first()

    if review is None:
        raise HTTPException(status_code=404, detail="La reseña no existe")
    
    return review

@router.put("/{id}", response_model=ReviewResponseModel)
async def modificar_review(id: int, modificacion: ReviewModificarModel):
    review = UserReview.select().where(UserReview.id == id).first()

    if review is None:
        raise HTTPException(status_code=404, detail="La reseña no existe")
    
    review.review = modificacion.review
    review.score = modificacion.score

    review.save()

    return review

@router.delete("/{id}", response_model = ReviewResponseModel)
async def eliminar_review(id: int):
    review = UserReview.select().where(UserReview.id == id).first()

    if review is None:
        raise HTTPException(status_code=404, detail="La reseña no existe")
    
    review.delete_instance()
    return review