# @param {Integer[]} arr
# @return {Boolean}
def unique_occurrences(arr)
    # hash -> count occurrence // O(n)
    # occurrence -> into set  // O(n)
    # compare hash size and occurrence set //O (1)
    count = Hash.new(0)
    arr.each do |element|
        count[element] += 1
    end

    occurences = count.values.to_set

    count.size == occurences.size
end