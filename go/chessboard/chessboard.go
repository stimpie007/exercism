package chessboard

type Rank = []bool
type Chessboard = map[string]Rank

func CountInRank(cb Chessboard, rank string) int {
	return counter(cb, func(r string, f int, val bool) bool {
		return rank == r && val
	})
}

func CountInFile(cb Chessboard, file int) int {
	return counter(cb, func(rank string, f int, val bool) bool {
		return file == f && val
	})
}

func CountAll(cb Chessboard) int {
	return counter(cb, func(rank string, file int, val bool) bool {
		return true
	})
}

func CountOccupied(cb Chessboard) int {
	return counter(cb, func(rank string, file int, val bool) bool {
		return val
	})
}

func counter(cb Chessboard, count func(rank string, file int, val bool) bool) int {
	var total int
	for key, rank := range cb {
		for i, file := range rank {
			if count(key, i+1, file) {
				total++
			}
		}
	}
	return total
}
