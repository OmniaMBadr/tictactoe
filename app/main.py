from dataclasses import dataclass
from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.models.tictactoe import TicTacToe


app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "OK"}


@dataclass
class RoundResponse:
    winner: str = "Player: X"
    board: str = "X | O | O\n- | X | O\n- | X | X\n"


responses = {
    500: {"description": "Something wrong happned."},
    200: {"content": {}, "description": "Run a TicTacToe round and return the winner if any and the board. "
                                        "<br>The board rows are separated by new line while the column values are separated by |. "
                                        "<br>'-' represents empty cell."
    }
}


@app.get("/tictactoe-round", response_model=RoundResponse, responses=responses)
def play_tictactoe_round():
    game = TicTacToe()
    try:
        winner = game.play()
        while not winner:
            winner = game.play()
    except Exception as ex:
        return JSONResponse(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            content={
                "message": f"Exception occured. {ex}.",
            })
    
    return JSONResponse(
        status_code=HTTPStatus.OK,
        content={
            "winner": str(winner),
            "board": str(game.board),
        })