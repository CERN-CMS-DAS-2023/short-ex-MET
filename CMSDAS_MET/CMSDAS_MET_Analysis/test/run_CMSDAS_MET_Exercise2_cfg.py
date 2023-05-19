import FWCore.ParameterSet.Config as cms

process = cms.Process("CMSDASMET")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.EventContent.EventContent_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1


process.TFileService = cms.Service("TFileService", fileName = cms.string("./outputs/cmsdas_met_exercise2_Summer20UL17.root") )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring((
        '/store/mc/RunIISummer20UL17MiniAODv2/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/40000/2C5565D7-ADE5-2C40-A0E5-BDFCCF40640E.root',
        '/store/mc/RunIISummer20UL17MiniAODv2/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/40000/F51FE4FE-0212-F94E-8367-67E84FE6FCE7.root',
        '/store/mc/RunIISummer20UL17MiniAODv2/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/40000/FE86B85E-8B55-4F4E-A911-FF8068F4EE46.root',
        '/store/mc/RunIISummer20UL17MiniAODv2/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/40000/0066C701-8B8A-3F42-AB75-9CF2FB14038A.root'
            )
                                      )
    )

process.cmsdasmetexercise2 = cms.EDAnalyzer('CMSDAS_MET_AnalysisExercise2',
                                    doprints = cms.bool(True),
                                    mets     = cms.InputTag("slimmedMETs")
                                    )

process.p = cms.Path(process.cmsdasmetexercise2)
