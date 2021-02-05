def solution(bridge_length, weight, truck_weights):
    answer = 0
    in_bridge_truck = []
    count = []

    while True:
        if not (truck_weights or in_bridge_truck):
            break
        answer += 1
        count = [i + 1 for i in count]
        if count and count[0] > bridge_length:
            del count[0]
            del in_bridge_truck[0]

        if truck_weights and sum(in_bridge_truck) + truck_weights[0] <= weight:
            in_bridge_truck.append(truck_weights[0])
            del truck_weights[0]
            count.append(1)
    return answer


if __name__ == '__main__':
    print(solution(2, 10, [7, 4, 5, 6]))
