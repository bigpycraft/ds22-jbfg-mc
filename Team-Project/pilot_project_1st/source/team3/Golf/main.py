import proj1st.team3.Golf_packages.regUser as regPlayer
import proj1st.team3.Golf_packages.getScore as getScore
import proj1st.team3.Golf_packages.regScore as regScore
import proj1st.team3.Golf_packages.regResult as regResult

# 플레이어 등록
player_list = regPlayer.regUsers() # 플레이어 등록

# calculator
randomScore, baseScore = getScore.getUserScore(player_list) # 플레이어 18홀 스코어 산출
strokeScore = getScore.getStroke(player_list, randomScore) # 플레이어 스트로크 산출
handyScore = getScore.getHandy(player_list) # 플레이어 핸디 점수 산출
score = getScore.getTotalScore(randomScore, handyScore, player_list) # 플레이어 최종스코어 산출
rank_list = getScore.getRank(score)
ebpbCnt = getScore.getEbpbCnt(player_list, randomScore, baseScore)

# 엑셀 '스코어' Sheet 결과 등록
regScore.regUserScores(randomScore, player_list)
regScore.regStroke(player_list, strokeScore)
regScore.regHandy(player_list, handyScore)
regScore.regTotalScore(player_list, score)
regScore.regRank(rank_list)
regScore.regEbpbCnt(player_list, ebpbCnt)

# 대회결과 시트
regResult.Result(player_list, score, rank_list, ebpbCnt)