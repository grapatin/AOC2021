lines = ARGF.readlines.map(&:chomp)

numbers = lines.shift.split(',').map(&:to_i)

boards = []

until lines.empty?
  lines.shift
  board = []
  5.times do
    board << lines.shift.strip.split(' ').map(&:to_i)
  end
  boards << board
end

def mark_number(board, number)
  board.each do |line|
    5.times do |index|
      line[index] = -1 if line[index] == number
    end
  end
end

def is_winning?(board)
  board.each do |line|
    return true if line.all? { |number| number == -1 }
  end

  5.times do |col|
    return true if board.all? { |line| line[col] == -1 }
  end

  false
end

def board_score(board)
  board.flatten.reject { |number| number == -1 }.sum
end

last_win = 0

until numbers.empty?
  number = numbers.shift

  winning_boards = []
  boards.map! do |board|
    mark_number board, number
    if is_winning?(board)
      winning_boards << board
      last_win = board_score(board) * number
      nil
    else
      board
    end
  end.compact!
end

puts last_win