import sys
input = sys.stdin.readline

def main():
    # 1) 입력
    n = int(input())
    cards = set(map(int, input().split()))
    m = int(input())
    queries = list(map(int, input().split()))
    
    # 2) 조회 및 결과 생성
    result = ['1' if q in cards else '0' for q in queries]
    
    # 3) 출력
    print(' '.join(result))

if __name__ == '__main__':
    main()
